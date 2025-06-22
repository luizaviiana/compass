class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor="Azul"):
        """
        Construtor da classe Aviao
        Parâmetros:
            modelo (str): modelo do avião
            velocidade_maxima (str): velocidade máxima do avião
            capacidade (int): número de passageiros
            cor (str): cor do avião, valor padrão "Azul"
        """
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor


# Criando os objetos da classe Aviao
aviao1 = Aviao("BOIENG456", "1500 km/h", 400)
aviao2 = Aviao("Embraer Praetor 600", "863 km/h", 14)
aviao3 = Aviao("Antonov An-2", "258 km/h", 12)

# Armazenando os objetos em uma lista
avioes = [aviao1, aviao2, aviao3]

# Iterando sobre a lista e imprimindo os objetos no formato fornecido
for aviao in avioes:
    print(
        f'O avião de modelo "{aviao.modelo}" possui uma velocidade máxima de '
        f'"{aviao.velocidade_maxima}", capacidade para "{aviao.capacidade}" passageiros '
        f'e é da cor "{aviao.cor}".'
    )
