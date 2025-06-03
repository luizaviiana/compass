def maiores_que_media(conteudo: dict)->list:
    """Retorna uma lista de produtos com preço acima da média e ordenados por preço"""
    valor_medio = sum(conteudo.values()) / len(conteudo)

    # Produtos com preço acima da média
    produtos_filtrados = filter(lambda item: item[1] > valor_medio, conteudo.items())

    # Ordena os produtos filtrados pelo preço (menor para maior)
    resultado = sorted(produtos_filtrados, key=lambda item: item[1])

    return resultado
