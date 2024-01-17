import requests
from tqdm import tqdm
import json
from datetime import datetime
import configparser

# Carregar as chaves do arquivo Chaves.ini
config = configparser.ConfigParser()
config.read('Chaves.ini')

app_key = config.get('API', 'app_key_pv')
app_secret = config.get('API', 'app_secret_pv')

base_url = 'http://appdevi3-implantacao.azurewebsites.net/odata/BuscaPrevendas'
headers = {
    'AppKey': app_key,
    'AppSecret': app_secret
}

preventa_numbers = ['39']

results = {}

for number in tqdm(preventa_numbers, desc="Processing", unit="request"):
    params = {
        'texto': '',
        'periodo': 'todas',
        '$orderby': 'Numero desc',
        '$count': 'true',
        '$filter': f'Numero eq {number}',
        '$select': 'Numero,PrevendaCabecalhoId,Cupom,Situacao'
    }

    url = f"{base_url}(texto='',periodo='todas')?{('&'.join([f'{k}={v}' for k, v in params.items()]))}"

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        results[number] = data
    else:
        print(f"Failed to fetch data for Prevena {number}. Status code: {response.status_code}")

# Salvando o resultado em um arquivo JSON com nome resultado_data.json
output_filename = f"resultadoPV_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
with open(output_filename, 'w') as output_file:
    json.dump(results, output_file)

print(f"\nResults saved to {output_filename}")
