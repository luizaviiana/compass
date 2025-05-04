class Ordenadora:

    def __init__(self, listaBaguncada):
        """
        Construtor da classe que recebe uma lista bagunçada
        """
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        """
        Retorna a lista com a ordenação dos valores em ordem crescente
        """
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        """
        Retorna a lista com a ordenação dos valores em ordem decrescente
        """
        return sorted(self.listaBaguncada, reverse=True)


# Instanciando os objetos
crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

# Chamando os métodos
ordenacao_crescente = crescente.ordenacaoCrescente()
ordenacao_decrescente = decrescente.ordenacaoDecrescente()

print(ordenacao_crescente)
print(ordenacao_decrescente)
