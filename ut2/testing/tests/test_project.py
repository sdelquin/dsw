import pytest
from django.test import Client
from django.utils.text import slugify
from model_bakery import baker
from pytest_django.asserts import assertContains, assertFormError, assertRedirects

from tasks.models import Task


@pytest.fixture
def task():
    return baker.make(Task, _fill_optional=True)


@pytest.mark.django_db
def test_task_model_has_proper_fields(client: Client, task):
    PROPER_FIELDS = (
        'id',
        'name',
        'description',
        'slug',
        'done',
        'complete_before',
        'created_at',
        'updated_at',
    )
    for field in PROPER_FIELDS:
        assert getattr(task, field) is not None


@pytest.mark.django_db
def test_root_url_redirects_to_task_list(client: Client):
    response = client.get('/')
    assertRedirects(response, '/tasks/')


@pytest.mark.django_db
def test_list_all_tasks(client: Client):
    DETAIL_URL = '/tasks/task/{slug}/'
    TOGGLE_URL = '/tasks/task/{slug}/toggle/'
    EDIT_URL = '/tasks/task/{slug}/edit/'
    DELETE_URL = '/tasks/task/{slug}/delete/'

    tasks = baker.make(Task, _quantity=10)
    response = client.get('/tasks/')
    assert response.status_code == 200
    for task in tasks:
        assertContains(response, task.name)
        assertContains(response, DETAIL_URL.format(slug=task.slug))
        assertContains(response, TOGGLE_URL.format(slug=task.slug))
        assertContains(response, EDIT_URL.format(slug=task.slug))
        assertContains(response, DELETE_URL.format(slug=task.slug))


@pytest.mark.django_db
def test_list_pending_tasks(client: Client):
    tasks = baker.make(Task, done=False, _quantity=10)
    response = client.get('/tasks/pending/')
    assert response.status_code == 200
    for task in tasks:
        assertContains(response, task.name)


@pytest.mark.django_db
def test_list_done_tasks(client: Client):
    tasks = baker.make(Task, done=True, _quantity=10)
    response = client.get('/tasks/done/')
    assert response.status_code == 200
    for task in tasks:
        assertContains(response, task.name)


@pytest.mark.django_db
def test_task_detail(client: Client, task):
    url = f'/tasks/task/{task.slug}/'
    response = client.get(url)
    assert response.status_code == 200
    assertContains(response, task.name)
    assertContains(response, task.description)
    assert response.context['task'] == task


@pytest.mark.django_db
def test_delete_task(client: Client, task):
    url = f'/tasks/task/{task.slug}/delete/'
    response = client.get(url)
    assert response.status_code in [200, 302]
    with pytest.raises(Task.DoesNotExist):
        Task.objects.get(pk=task.pk)


@pytest.mark.django_db
def test_add_task_with_get_method(client: Client):
    response = client.get('/tasks/add/')
    assert response.status_code == 200
    assert response.context['form']
    assert 'name' in response.context['form'].fields
    assert 'description' in response.context['form'].fields
    assert 'slug' not in response.context['form'].fields
    assert 'done' not in response.context['form'].fields


@pytest.mark.django_db
def test_add_task_with_post_method(client: Client):
    task = baker.prepare(Task, _fill_optional=True)
    payload = dict(
        name=task.name, description=task.description, complete_before=task.complete_before
    )
    response = client.post('/tasks/add/', payload)
    assertRedirects(response, '/tasks/')
    latest_task = Task.objects.latest('pk')
    assert latest_task.name == task.name
    assert latest_task.slug == slugify(task.name)
    assert latest_task.description == task.description
    assert latest_task.complete_before == task.complete_before
    assert latest_task.created_at is not None
    assert latest_task.updated_at is not None


@pytest.mark.django_db
def test_add_task_fails_when_missing_required_fields(client: Client):
    response = client.post('/tasks/add/')
    assert response.status_code == 200
    assertFormError(response.context['form'], 'name', 'This field is required.')


@pytest.mark.django_db
def test_edit_task_with_get_method(client: Client, task):
    url = f'/tasks/task/{task.slug}/edit/'
    response = client.get(url)
    assert response.status_code == 200
    form_values = response.context['form'].initial.values()
    assert task.name in form_values
    assert task.description in form_values


@pytest.mark.django_db
def test_edit_task_with_post_method(client: Client, task):
    form_task = baker.prepare(Task, _fill_optional=True)
    payload = dict(
        name=form_task.name,
        description=form_task.description,
        done=form_task.done,
        complete_before=form_task.complete_before,
    )
    url = f'/tasks/task/{task.slug}/edit/'
    response = client.post(url, payload)
    assert response.status_code in [200, 302]
    edited_task = Task.objects.get(pk=task.pk)
    assert edited_task.name == form_task.name
    assert edited_task.slug == slugify(form_task.name)
    assert edited_task.description == form_task.description
    assert edited_task.done == form_task.done
    assert edited_task.complete_before == form_task.complete_before
    assert edited_task.updated_at > edited_task.created_at


@pytest.mark.django_db
def test_edit_task_fails_when_missing_required_fields(client: Client, task):
    url = f'/tasks/task/{task.slug}/edit/'
    response = client.post(url)
    assert response.status_code == 200
    assertFormError(response.context['form'], 'name', 'This field is required.')


@pytest.mark.django_db
def test_toggle_task(client: Client, task):
    url = f'/tasks/task/{task.slug}/toggle/'
    response = client.get(url)
    assert response.status_code in [200, 302]
    assert Task.objects.get(pk=task.pk).done is not task.done
