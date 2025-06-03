from functools import reduce


def calcula_saldo(lancamentos) -> float:
    """
    Calcula o saldo final a partir de uma lista de lançamentos bancários
    Parâmetros:
        lancamentos (list): Lista de tuplas (valor, tipo)
    Retorno:
        float: saldo bancário final após os lançamentos
    """
    operacoes = map(
        lambda transacao: transacao[0] if transacao[1] == 'C' else -transacao[0],
        lancamentos
    )

    # Reduce para somar todos os valores da lista operacoes
    saldo = reduce(lambda acumulado, valor: acumulado + valor, operacoes)

    # Saldo final
    return saldo
