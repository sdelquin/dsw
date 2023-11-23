import json
import re
from decimal import Decimal, InvalidOperation

from django.http import HttpResponseBadRequest
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@require_POST
@csrf_exempt
def incoming_transfer(request):
    BANK_ID = 0
    REQUIRED_FIELDS = ('sender', 'cac', 'concept', 'amount')

    data = json.loads(request.body)
    for field in REQUIRED_FIELDS:
        if field not in data:
            return HttpResponseBadRequest(f'Field "{field}" not in request')
        if not data[field].strip():
            return HttpResponseBadRequest(f'Field "{field}" has no value')
    if not re.fullmatch(rf'A{BANK_ID}-\d{{4}}', cac := data['cac']):
        return HttpResponseBadRequest(f'CAC "{cac}" does not exist in our bank')
    try:
        Decimal(amount := data['amount'])
    except InvalidOperation:
        return HttpResponseBadRequest(
            f'Invalid value "{amount}" for field "amount": decimal value expected'
        )
    return HttpResponse('✅ Transfer successfully processed')
