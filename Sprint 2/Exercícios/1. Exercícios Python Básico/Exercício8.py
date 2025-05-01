def valores(*args, **kwargs):
    """
    Essa função imprime o valor de cada parâmetro recebido, nomeados ou não.

    Parâmetros:
        *args: Argumentos não nomeados.
        **kwargs: Argumentos nomeados.
    """
    for valor in args:
        print(valor)

    for valor in kwargs.values():
        print(valor)


valores(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
