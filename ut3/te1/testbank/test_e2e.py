import pytest
import requests


@pytest.fixture
def transfer_url():
    BANK_URL = 'http://localhost:8000/'
    return BANK_URL + 'transfer/incoming/'


@pytest.fixture
def payload():
    return dict(sender='Google Inc.', cac='A0-0001', concept='Invoice 341', amount='500')


def test_transfer_works_fine(transfer_url, payload):
    response = requests.post(transfer_url, json=payload)
    assert response.status_code == 200
    assert response.text == '✅ Transfer successfully processed'


def test_transfer_fails_when_missing_fields(transfer_url, payload):
    response = requests.post(transfer_url, json=payload.pop('sender'))
    assert response.status_code == 400
    assert response.text == 'Field "sender" not in request'


def test_transfer_fails_when_empty_values(transfer_url, payload):
    payload['sender'] = '  '
    response = requests.post(transfer_url, json=payload)
    assert response.status_code == 400
    assert response.text == 'Field "sender" has no value'


def test_transfer_fails_when_cac_does_not_exist(transfer_url, payload):
    payload['cac'] = 'B0-0001'
    response = requests.post(transfer_url, json=payload)
    assert response.status_code == 400
    assert response.text == 'CAC "B0-0001" does not exist in our bank'


def test_transfer_fails_when_amount_is_not_decimal(transfer_url, payload):
    payload['amount'] = 'hello'
    response = requests.post(transfer_url, json=payload)
    assert response.status_code == 400
    assert response.text == 'Invalid value "hello" for field "amount": decimal value expected'


def test_transfer_fails_when_request_is_not_post(transfer_url, payload):
    response = requests.get(transfer_url, json=payload)
    assert response.status_code == 405
