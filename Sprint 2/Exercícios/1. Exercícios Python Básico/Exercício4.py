def remove_duplicados(lista_fornecida):
    """
    Remove elementos duplicados de uma lista, utilizando a estrutura set.
    Parâmetros:
        lista_fornecida (list): Lista fornecida podendo existir elementos
        duplicados.
    Retorna:
        list: Nova lista contendo apenas os elementos únicos da original.
    """
    sem_duplicados = set(lista_fornecida)
    lista_sem_duplicados = list(sem_duplicados)
    return lista_sem_duplicados


lista_exercicio = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remove_duplicados(lista_exercicio)

print(resultado)
