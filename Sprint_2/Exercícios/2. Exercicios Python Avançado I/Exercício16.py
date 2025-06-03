class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None

    @property
    def nome(self):
        """
        Retorna o valor do atributo privado __nome
        """
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """
        Define o valor do atributo privado __nome
        """
        self.__nome = valor


pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
