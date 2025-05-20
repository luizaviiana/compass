import hashlib

print("Bem-vindo ao mascarador de palavras!")

while True:
    try:
        input_usuario = input('Qual texto deseja mascarar? Se preferir encerrar digite "sair" : ')
       
        if input_usuario.lower() == 'sair':
            print("Obrigado por usar o mascarador de palavras. Até logo!")
            break

        codigo_mascarado = hashlib.sha1(input_usuario.encode()).hexdigest()
        print("Seu código mascarado é: ", codigo_mascarado) 
    except Exception as excecao:
        print(f"Erro durante o processamento: {excecao}")
