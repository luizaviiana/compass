def dividir_lista(lista):
    """
    Função que recebe como parâmetro uma lista e retorna 3 listas:
    a lista recebida dividida em 3 partes iguais
    Parâmetro:
        lista (list): Lista fornecida que será dividida em três partes iguais
        (deve ser divisível por três)
    Retorna:
        tuple: Três listas provenientes da original, porém em partes
    """
    tamanho_lista = len(lista)
    parte = tamanho_lista // 3

    primeira_parte = lista[:parte]
    segunda_parte = lista[parte:2 * parte]
    terceira_parte = lista[2 * parte:]

    return primeira_parte, segunda_parte, terceira_parte


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

parte_1, parte_2, parte_3 = dividir_lista(lista)

print(parte_1, parte_2, parte_3)
