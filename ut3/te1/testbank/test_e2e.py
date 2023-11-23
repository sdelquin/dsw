import requests

BANK_URL = 'http://localhost:8000/'
TRANSFER_URL = BANK_URL + 'transfer/incoming/'
PAYLOAD = dict(sender='Google Inc.', cac='A0-0001', concept='Invoice 341', amount='500')


def test_transfer_works_fine():
    response = requests.post(TRANSFER_URL, json=PAYLOAD)
    assert response.status_code == 200
    assert response.text == '✅ Transfer successfully processed'


def test_transfer_fails_when_missing_fields():
    payload = PAYLOAD.copy()
    response = requests.post(TRANSFER_URL, json=payload.pop('sender'))
    assert response.status_code == 400
    assert response.text == 'Field "sender" not in request'


def test_transfer_fails_when_empty_values():
    payload = PAYLOAD.copy()
    payload['sender'] = '  '
    response = requests.post(TRANSFER_URL, json=payload)
    assert response.status_code == 400
    assert response.text == 'Field "sender" has no value'


def test_transfer_fails_when_cac_does_not_exist():
    payload = PAYLOAD.copy()
    payload['cac'] = 'B0-0001'
    response = requests.post(TRANSFER_URL, json=payload)
    assert response.status_code == 400
    assert response.text == 'CAC "B0-0001" does not exist in our bank'


def test_transfer_fails_when_amount_is_not_decimal():
    payload = PAYLOAD.copy()
    payload['amount'] = 'hello'
    response = requests.post(TRANSFER_URL, json=payload)
    assert response.status_code == 400
    assert response.text == 'Invalid value "hello" for field "amount": decimal value expected'
