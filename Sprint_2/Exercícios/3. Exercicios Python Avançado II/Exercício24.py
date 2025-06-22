def relatorio_notas():
    """
    Processa o arquivo 'estudantes.csv' e imprime para cada estudante
    as 3 maiores notas e a média dessas notas com duas casas
    """
    with open('estudantes.csv', 'r', encoding='utf-8') as arquivo:
        linhas_csv = arquivo.readlines()

    linhas_limpas = list(map(lambda linha: linha.strip(), linhas_csv))

    dados_processados = list(map(
        lambda linha: (
            linha.split(',')[0],  # Nome
            list(map(int, linha.split(',')[1:]))  # Lista de 5 notas
        ),
        linhas_limpas
    ))

    # Ordenando alfabeticamente pelo nome
    dados_ordenados = sorted(dados_processados, key=lambda dado: dado[0])

    # Itera sobre cada estudante para realizar os cálculos
    for estudante, avaliacoes in dados_ordenados:
        top_3_notas = sorted(avaliacoes, reverse=True)[:3]
        media_top_3 = round(sum(top_3_notas) / 3, 2)
        print(f'Nome: {estudante} Notas: {top_3_notas} Média: {media_top_3}')


# Executando a função
relatorio_notas()
