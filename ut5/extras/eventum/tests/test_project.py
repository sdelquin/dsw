import datetime

import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import (
    assertContains,
    assertFormError,
    assertRedirects,
    assertTemplateUsed,
)

from events.forms import AddEventForm
from events.models import Event

# https://djangostars.com/blog/django-pytest-testing/
# https://docs.djangoproject.com/en/5.0/topics/testing/tools/#assertions


@pytest.mark.django_db
def test_root_redirect(client: Client):
    response = client.get('/')
    assertRedirects(response, reverse('events:list'))


@pytest.mark.django_db
def test_event_list(client: Client, events: dict):
    response = client.get(reverse('events:list'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'events/list.html')
    for event in events:
        assertContains(response, event['fields']['name'])
    assertContains(response, 'important!')
    assertContains(response, 'Add new event')


@pytest.mark.django_db
def test_event_detail(client: Client, events: dict):
    event_fixture = events[0]
    event = Event.objects.get(pk=event_fixture['pk'])
    response = client.get(reverse('events:detail', args=[event]))
    assert response.status_code == 200
    assert response.context['event'] == event
    assertTemplateUsed(response, 'events/detail.html')
    assertContains(response, event_fixture['fields']['name'])
    assertContains(response, 'Back to event list')


@pytest.mark.django_db
def test_display_form_when_adding_new_event(client: Client):
    response = client.get(reverse('events:add'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'events/add.html')
    assert isinstance(response.context['form'], AddEventForm)
    response_form = response.context['form']
    assert not response_form.data  # form is unbound
    form = AddEventForm()
    assert response_form.fields.keys() == form.fields.keys()


@pytest.mark.django_db
def test_add_event_fails_when_missing_data(client: Client):
    response = client.post(reverse('events:add'))
    assertFormError(response, 'form', 'name', 'This field is required.')
    assertFormError(response, 'form', 'date', 'This field is required.')


@pytest.mark.django_db
def test_add_event(client: Client):
    event_fields = dict(
        name='Test event', date='2024-10-01', description='pytest django', important=True
    )
    latest_event_pk = Event.objects.latest('pk').pk
    response = client.post(reverse('events:add'), event_fields)
    assertRedirects(response, reverse('events:list'))
    event = Event.objects.latest('pk')
    assert event.pk == latest_event_pk + 1
    for field, value in event_fields.items():
        value = datetime.date(*(int(d) for d in value.split('-'))) if field == 'date' else value  # type: ignore
        assert getattr(event, field) == value
