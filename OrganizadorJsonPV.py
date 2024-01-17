import json

# Carregue o JSON existente
with open('resultadoPV_20240117142956.json', 'r') as arquivo:
    dados_json = json.load(arquivo)

# Crie uma lista para armazenar os novos dicionários
novos_json = []

# Iterar sobre cada chave do JSON
for chave, valor in dados_json.items():
    # Acesse a lista dentro da chave 'value'
    lista_pre_venda = valor['value']

    # Iterar sobre cada item da lista
    for item in lista_pre_venda:
        # Criar um novo dicionário apenas com os campos desejados
        novo_json = {
            'Numero': item['Numero'],
            'PrevendaCabecalhoId': item['PrevendaCabecalhoId'],
            'Situacao': item['Situacao'],
            'Cupom': item['Cupom']
        }
        novos_json.append(novo_json)

# Salvar o novo JSON reorganizado
with open('resultadoPV.json', 'w') as novo_arquivo:
    json.dump(novos_json, novo_arquivo, indent=2)
