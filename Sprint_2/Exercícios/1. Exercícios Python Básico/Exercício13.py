import random

random_list = random.sample(range(500), 50)

lista_ordenada = sorted(random_list)

valor_minimo = min(lista_ordenada)
valor_maximo = max(lista_ordenada)
media = round(sum(lista_ordenada) / len(lista_ordenada), 2)

meio = len(lista_ordenada) // 2
if len(lista_ordenada) % 2 == 0:
    mediana = (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
else:
    mediana = lista_ordenada[meio]

print(
    f"Media: {media:.2f}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}"
)
