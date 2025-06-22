with open('number.txt', 'r') as arquivo:
    valores = list(map(int, arquivo.readlines()))

filtrados = list(filter(lambda numero: numero % 2 == 0, valores))
top_5_pares = sorted(filtrados, reverse=True)[:5]

print(top_5_pares)
print(sum(top_5_pares))
