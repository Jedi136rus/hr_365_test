from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

API_URL = 'https://api.currencyapi.com/v3/latest?'
RATES = 'base_currency=EUR&currencies=USD'
API_KEY = 'cur_live_XKf0Vm1furR8r1Q8WolbFzwqEzKv6bRrCuuaRvlO'
header_api = {'apikey': API_KEY}
# /api/rates?from=USD&to=RUB&value=1


def get_exchange_rate(from_cur: str, to_cur: str) -> float:
    """
    Функция принимает две валюты на вход
    и возвращает число - обменный курс
    (было взято апи currency, позволяет
    сделать до 300 запросов в день),
    если необходимо можно переделать на
    парсинг какой-нибудь биржи (создать другое свое апи)
    :param from_cur: код исходной валюты
    :param to_cut: код конечной валюты
    :return: число равное обменному курсу
    """
    rate_params = f'base_currency={from_cur.upper()}&currencies={to_cur.upper()}'
    res = requests.get(url=API_URL+rate_params, headers=header_api)
    if res.status_code == 200:
        return res.json()['data'][to_cur.upper()]['value']
    elif res.status_code == 422:
        return -1
    else:
        raise KeyError


@api_view(['GET'])
def convert_value(request):
    from_val = request.GET.get("from", None)
    if from_val is None:
        return Response({'error': 'add "from" param'}, status=status.HTTP_404_NOT_FOUND)
    to_val = request.GET.get('to', None)
    if to_val is None:
        return Response({'error': 'add "to" param'}, status=status.HTTP_404_NOT_FOUND)
    cur_val = request.GET.get('value', None)
    if cur_val is None:
        return Response({'error': 'add "value" param'}, status=status.HTTP_404_NOT_FOUND)
    try:
        cur_val = float(cur_val)
    except ValueError:
        return Response({'error': 'param "value" must be int or float'})

    try:
        res = get_exchange_rate(from_cur=from_val, to_cur=to_val)*cur_val
    except KeyError:
        return Response({'error': 'incorrect input'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    if res < 0:
        return Response({'error': 'please use correct currency code'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    data = {
        'result': round(res, 2),
    }
    return Response(data, status=status.HTTP_200_OK)
