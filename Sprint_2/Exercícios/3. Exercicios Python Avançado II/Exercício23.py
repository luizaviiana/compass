def calcular_valor_maximo(operadores, operandos) -> float:
    """
    Recebe uma lista de operadores e uma lista de operandos, na qual
    as operações são aplicadas à lista de operadores nas respectivas
    posições e retorna o maior valor
    """

    operacoes = zip(operadores, operandos)

    resultados = map(
        lambda operacao: eval(f"{operacao[1][0]}{operacao[0]}{operacao[1][1]}"),
        operacoes
    )

    return max(resultados)


# Listas fornecidas com operadores e operandos
operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print(calcular_valor_maximo(operadores, operandos))
