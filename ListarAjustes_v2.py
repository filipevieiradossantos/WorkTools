import requests
import json
from tqdm import tqdm
import configparser

# Carregar as chaves do arquivo Chaves.ini
config = configparser.ConfigParser()
config.read('Chaves.ini')

app_key = config.get('API', 'app_key')
app_secret = config.get('API', 'app_secret')

url = "https://app.omie.com.br/api/v1/estoque/ajuste/"
headers = {'Content-type': 'application/json'}

payload = {
    "call": "ListarAjusteEstoque",
    "app_key": app_key,
    "app_secret": app_secret
}

resultados = []
total_paginas = 1

for pagina in tqdm(range(1, total_paginas + 1), desc="Progresso"):
    payload["param"] = [{"pagina": pagina, "registros_por_pagina": 1000, "apenas_importado_api": "N"}]

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        resultados.append(response.json())
    else:
        print(f"Falha na requisição para a página {pagina}. Código de status: {response.status_code}")

with open('resultadoListarAjustes.json', 'w') as file:
    json.dump(resultados, file, indent=2)
