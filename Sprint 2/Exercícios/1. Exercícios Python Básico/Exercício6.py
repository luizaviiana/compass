def my_map(list, f):
    """
    Irá aplicar a função f para cada elemento da lista e retorna o resultado
    em uma nova lista.

    Parâmetros:
        list: Lista de entrada
        f: Função que será aplicada a cada elemento da lista.
    Retorna:
        list: Nova lista com os resultados da aplicação da função f.
    """
    resultado = []

    for elemento in list:
        resultado.append(f(elemento))

    return resultado


entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def numero_ao_quadrado(numero):
    """Retorna o número elevado ao quadrado."""
    return numero ** 2


resultado = my_map(entrada, numero_ao_quadrado)

print(resultado)
