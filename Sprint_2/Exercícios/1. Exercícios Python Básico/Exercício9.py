class Lampada:
    """
    Representa o comportamento da lâmpada  (ligada ou desligada)
    """
    def __init__(self, ligada: bool):
        """
        Inicializa a lâmpada com o estado informado
        Parâmetros:
            ligada (bool): True para lâmpada ligada e False para desligada
        """
        self.ligada = ligada

    def liga(self):  # Liga a lâmpada
        self.ligada = True

    def desliga(self):  # Desliga a lâmpada
        self.ligada = False

    def esta_ligada(self):  # verificação se está ligada
        return self.ligada


# Testando a classe
minha_lampada = Lampada(False)

minha_lampada.liga()
print("A lâmpada está ligada?", minha_lampada.esta_ligada())

minha_lampada.desliga()
print("A lâmpada ainda está ligada?", minha_lampada.esta_ligada())
