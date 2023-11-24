import pytest
from django.test import Client
from django.urls import reverse

# https://djangostars.com/blog/django-pytest-testing/


@pytest.fixture
def payload():
    return dict(sender='Google Inc.', cac='A0-0001', concept='Invoice 341', amount='500')


def test_transfer_works_fine(client: Client, payload: dict[str, str]):
    url = reverse('transfer:incoming_transfer')
    response = client.post(url, payload, content_type='application/json')
    assert response.status_code == 200


def test_transfer_fails_when_missing_fields(client: Client, payload: dict[str, str]):
    url = reverse('transfer:incoming_transfer')
    payload.pop('sender')
    response = client.post(url, payload, content_type='application/json')
    assert response.status_code == 400
    assert response.content.decode() == 'Field "sender" not in request'


def test_transfer_fails_when_empty_values(client: Client, payload: dict[str, str]):
    url = reverse('transfer:incoming_transfer')
    payload['sender'] = '  '
    response = client.post(url, payload, content_type='application/json')
    assert response.status_code == 400
    assert response.content.decode() == 'Field "sender" has no value'


def test_transfer_fails_when_cac_does_not_exist(client: Client, payload: dict[str, str]):
    url = reverse('transfer:incoming_transfer')
    payload['cac'] = 'B0-0001'
    response = client.post(url, payload, content_type='application/json')
    assert response.status_code == 400
    assert response.content.decode() == 'CAC "B0-0001" does not exist in our bank'


def test_transfer_fails_when_amount_is_not_decimal(client: Client, payload: dict[str, str]):
    url = reverse('transfer:incoming_transfer')
    payload['amount'] = 'hello'
    response = client.post(url, payload, content_type='application/json')
    assert response.status_code == 400
    assert (
        response.content.decode()
        == 'Invalid value "hello" for field "amount": decimal value expected'
    )


def test_transfer_fails_when_request_is_not_post(client: Client, payload: dict[str, str]):
    url = reverse('transfer:incoming_transfer')
    response = client.get(url, payload, content_type='application/json')
    assert response.status_code == 405
