class Passaro:
    """
    Superclasse contendo as habilidades de voar e emitir som.
    """
    def voar(self):
        """Imprime que o pássaro está voando."""
        print("Voando...")

    def emitir_som(self):
        """
        Método a ser implementado pelas subclasses
        """
        pass


class Pato(Passaro):
    """
    Classe que representa um Pato, herda de Passaro.
    """
    def emitir_som(self):
        """Imprime o som do pato."""
        print("Pato emitindo som...")
        print("Quack Quack")


class Pardal(Passaro):
    """
    Classe que representa um Pardal, herda de Passaro.
    """
    def emitir_som(self):
        """Imprime o som do pardal."""
        print("Pardal emitindo som...")
        print("Piu Piu")


"""Testando as classes"""
print("Pato")
pato = Pato()
pato.voar()
pato.emitir_som()

print("Pardal")
pardal = Pardal()
pardal.voar()
pardal.emitir_som()
