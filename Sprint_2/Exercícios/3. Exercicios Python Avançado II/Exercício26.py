def pares_ate(n: int):
    """Gera números pares de 2 até n usando generator"""
    for numero in range(2, n + 1, 2):
        yield numero
