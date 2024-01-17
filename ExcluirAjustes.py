import requests
import configparser

# Carregar as chaves do arquivo Chaves.ini
config = configparser.ConfigParser()
config.read('Chaves.ini')

app_key = config.get('API', 'app_key')
app_secret = config.get('API', 'app_secret')

# Obtenha os IDs do usuário separados por vírgula
ids_input = input("Informe os números de IDs separados por vírgula: ")
ids = ids_input.split(',')

# URL da API
url = "https://app.omie.com.br/api/v1/estoque/ajuste/"

# Faça a solicitação para cada ID
for id_ajuste in ids:
    # Estrutura dos dados
    data = {
        "call": "ExcluirAjusteEstoque",
        "app_key": app_key,
        "app_secret": app_secret,
        "param": [{"id_ajuste": int(id_ajuste)}]
    }

    # Enviar a solicitação POST usando a biblioteca requests
    response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

    # Exibir o resultado
    print(response.text)
