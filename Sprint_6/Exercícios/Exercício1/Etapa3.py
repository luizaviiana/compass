import random
import time
import os
import names

random.seed(40)

qtd_nomes_unicos = 39080
qtd_nomes_aleatorios = 10000000

print(f"Gerando {qtd_nomes_unicos} nomes únicos")
nomes_unicos = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")
nomes_aleatorios = [random.choice(nomes_unicos) for _ in range(qtd_nomes_aleatorios)]

nome_arquivo = "nomes_aleatorios.txt"

print(f"Salvando nomes no arquivo '{nome_arquivo}'")
with open(nome_arquivo, "w", encoding="utf-8") as f:
    for nome in nomes_aleatorios:
        f.write(nome + "\n")

print("Arquivo gerado com sucesso.")
