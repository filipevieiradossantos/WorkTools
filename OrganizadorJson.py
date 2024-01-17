import json

# Carregue o JSON existente
with open('resultadoListarAjustes.json', 'r') as arquivo:
    dados_json = json.load(arquivo)

# Acesse a lista dentro da chave 'ajuste_estoque_lista'
ajuste_lista = dados_json[0]['ajuste_estoque_lista']

# Crie uma lista para armazenar os novos dicionários
novos_json = []

# Iterar sobre cada item da lista
for item in ajuste_lista:
    # Verificar se 'obs' e 'id_ajuste' estão presentes antes de acessá-los
    if 'obs' in item and 'id_ajuste' in item:
        novo_json = {
            'obs': item['obs'],
            'id_ajuste': item['id_ajuste']
        }
        novos_json.append(novo_json)

# Salvar o novo JSON reorganizado
with open('novoseuarquivoListarAjustes.json', 'w') as novo_arquivo:
    json.dump(novos_json, novo_arquivo, indent=2)
