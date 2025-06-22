def soma_numeros(numeros_str):
    """
     função que recebe uma string de números separados por vírgula
     e retorna a soma de todos eles
     Parâmetros:
        numeros_str (str): "1,3,4,6,10,76,..."
     Retorna:
        int: A soma dos valores inteiros
    """
    lista_numeros = numeros_str.split(',')
    lista_inteiros = [int(numero) for numero in lista_numeros]
    return sum(lista_inteiros)


entrada = "1,3,4,6,10,76"
soma = soma_numeros(entrada)

print(soma)
