import requests
import json


class ImportaClima:

    def __init__(self, cidade):
        self.cidade = cidade
        ImportaClima.requisitar_clima(self)
        ImportaClima.extrair_informacoes(self)

    def requisitar_clima(self):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        argumentos = {"q": f"{self.cidade},br",
                      "lat": "0",
                      "lon": "0",
                      "callback": "",
                      "id": f"",
                      "lang": "pt",
                      "units": "metric",
                      "mode": "json"}

        headers = {
            'x-rapidapi-key': "30068c84dfmshc3ec9f0fde30cadp1d9e7fjsn1fa8beb53935",
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

        resposta = requests.request("GET", url, headers=headers, params=argumentos)
        resposta = resposta.text
        return resposta

    def extrair_informacoes(self):
        dicionario_clima = json.loads(ImportaClima.requisitar_clima(self))
        local = dicionario_clima['name']

        dicionario_main = dicionario_clima['main']
        temp = dicionario_main['temp']
        feeks_like = dicionario_main['feels_like']
        temp_min = dicionario_main['temp_min']
        temp_max = dicionario_main['temp_max']
        humidity = dicionario_main['humidity']

        print(f'A cidade buscada é {local}\n'
              f'Temperatura atual: {temp}°C\n'
              f'Máxima: {temp_max}°C\n'
              f'Mínima: {temp_min}°C\n'
              f'Sensação térmica: {feeks_like}°C\n'
              f'Humidade relativa: {humidity}%\n')
