import json

with open('person.json', 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)

print(conteudo)
