def conta_vogais(texto: str) -> int:
    """
    Conta o número de vogais em uma string.
    Parâmetros:
    texto (str): Texto a ser analisado.
    Retorno:
    int: Quantidade de vogais encontradas.
    """
    vogais = filter(lambda letra: letra.lower() in 'aeiou', texto)
    return len(list(vogais))
