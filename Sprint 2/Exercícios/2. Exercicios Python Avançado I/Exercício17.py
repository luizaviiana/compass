class Calculo:
    def somando(self, x, y):
        """Recebe dois parâmetros, X e Y, e retorna a soma dos dois."""
        return x + y

    def subtraindo(self, x, y):
        """Recebe dois parâmetros, X e Y, e retorna a subtração dos dois."""
        return x - y


"""Testando a clase"""
x = 4
y = 5

operacao = Calculo()

soma = operacao.somando(x, y)
subtracao = operacao.subtraindo(x, y)

print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
