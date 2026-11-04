# Integração com a API

'''
import requests

resposta = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params="latitude:" "52,52",
    "longitude:" "13,41",
    "timezone:" "Not set (GMT+0)",
    "temperature_2m:" "°C",
    timeout=15
)

resposta.raise_for_status

dados = requests.json()

valor = dados["chave"]
'''