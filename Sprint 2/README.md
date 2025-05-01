# 🚀 Sprint 2

## 📌 Resumo

Durante a Sprint 2, pude aprofundar um pouco mais sobre a linguagem de progragamação Python por meio de cursos, exercícios e desafios. Apesar de já ter estudado alguns conceitos anteriormente, por meio dessa sprint consolidei ainda mais os meus conhecimentos de uma forma dinâmica, prática e colaborativa, uma vez que constantemente estava discutindo sobre os exercicios e dificuldades com os meus colegas da squad. A seguir estarei detalhando um pouco mais sobre os principais conteúdos abordados:

- **Data & Analytics - Conceitos de Python**: 

- **Python 3 - Curso Completo do Básico ao Avançado**: 

- **Curso Ciência de Dados para Iniciantes**: 

- **Estatística Descritiva com Python**: 

- **Curso de Lógica de Programação**: 

🤔 *Reflexões*



---

## 🗂️ Sumário 

1. [Desafio](#desafio)
2. [Exercícios](#exercícios)
    - 2.1 [Exercícios Python Básico](#21-exercícios-python-básico)
    - 2.2 [Exercícios Python Avançado I](#22-exercícios-python-avançado-i)
    - 2.3 [Exercícios Python Avançado II](#23-exercícios-python-avançado-ii)
    - 2.4 [Exercícios Python ETL](#24-exercícios-python-etl)

3. [Evidências](#evidências)
    - 3.1 [Exercícios Python Básico](#31-exercícios-python-básico)
    - 3.2 [Exercícios Python Avançado I](#32-exercícios-python-avançado-i)
    - 3.3 [Exercícios Python Avançado II](#33-exercícios-python-avançado-ii)
    - 3.4 [Exercícios Python ETL](#34-exercícios-python-etl)

4. [Certificados](#certificados)

---

# [Desafio](./Desafio/) 

No desafio dessa sprint 2 foi pedido...

O arquivo desenvolvido e utilizado para realização do desafio está disponível na pasta *Desafio*, as evidências do desafio encontram-se na pasta *Evidências* e a sua documentação é apresentada no seu README.md. Segue os links:

- [Desafio](./Desafio/) 
- [Evidências](./Evidências/)
- [Readme Desafio](./Desafio/README.md)

Esse desafio foi bastante interessante, pude .....


---

# [Exercícios](./Exercícios/)

## 2.1 Exercícios Python Básico


1. Dada a seguinte lista:
<br>
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
<br>
Faça um programa que gere uma nova lista contendo apenas números ímpares.

>Resolução: No enunciado é fornecida uma lista e  pedido uma nova lista apenas com números ímpares. Para resolução é necessário percorrer cada elemento da lista a, para fazer iteração utilizei o for, fiz a verificação do número ímpar fazendo o resto da divisão por 2 diferente de 0, por meio do operador módulo (%). Por fim, o append adiciona o número na lista se o resultado da condição for verdadeiro.

[Resposta Ex.1](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício1.py)

2. Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

> Resolução: Inicialmente criei uma lista com as palavras fornecidas, percorri cada palavra da lista usando o for, adicionei uma condicional para comparar a palavra com sua versão invertida, se fosse verdadeira retornaria palíndromo, senão, retornaria que não é palíndromo.

[Resposta Ex.2](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício2.py)


3. Dada as listas a seguir:
<br>
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
<br>
Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

> Resolução: Antes de começar o código confirmei que todas as listas tinham o mesmo tamanho, após isso iniciei de fato. Para começar, utilizei a função enumerate para percorrer a lista ao mesmo tempo que acessa o índice de cada elemento, toda vez que o for rodar ele irá pegar o índice e cada elemento correspondente ao valor dele nas listas.

[Resposta Ex.3](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício3.py)

4. Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função:
<br>
['abc', 'abc', 'abc', '123', 'abc', '123', '123']

> Resolução: Defini uma função que recebe uma lista como entrada, fiz uso do set para converter a lista em conjunto e eliminar automaticamente os elementos repetidos, depois converti o conjunto novamente em uma lista, retornando a nova lista sem duplicados. Além disso, utilizei docstring para documentação interna da função.

[Resposta Ex.4](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício4.py)

5. Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

> Resolução: Primeiramente importei o módulo json. Após isso,  usei with open() para abrir e fechar o arquivo automaticamente, a função open possui dois parâmetros obrigatórios: o filename (person.json) e o mode (modo leitura), além desses utilizei utf-8 para garantir que os caracteres especiais fossem lidos corretamente. Por fim, converti o conteúdo do arquivo json em um dicionário python e fiz a exibição.

[Resposta Ex.5](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício5.py)

6. Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.
<br>
Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

> Resolução: Criei a função my_map(list, f) na qual  inicia com uma lista vazia para armazenar os resultados, por meio do for é feita a iteração dos elementos da lista aplicando a função em cada um e adicionando o resultado na nova lista. Após isso, passei a lista de entrada e a função que será aplicada em cada elemento, finalizei fazendo a impressão do resultado final

[Resposta Ex.6](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício6.py)

7. Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

> Resolução: Seguindo a mesma lógica da questão 5, usei with open() para abrir e fechar o arquivo automaticamente, a função open possui dois parâmetros obrigatórios: o filename (arquivo_texto.txt) e o mode (modo leitura), além desses utilizei utf-8 para garantir que os caracteres especiais fossem lidos corretamente. Por fim, fiz a leitura do arquivo como uma string e na função print passei o parâmetro end="" para que a próxima saída seja impressa na mesma linha.

[Resposta Ex.7](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício7.py)

8. Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido. Teste sua função com os seguintes parâmetros:
<br>
(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

> Resolução: Para resolução da questão defini a função valores, que usa o *args para armazenar parâmetros não nomeados e **kwargs para armazenamento de parâmetros nomeados, realizei a iteração sobre o *args por meio do for e fiz o mesmo no **kwargs, porém adicionei o .values() para retornar somente os valores do dicionário e finalizei ambos com a impressão dos valores.

[Resposta Ex.8](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício8.py)

>9. 

Resolução: 

[Resposta Ex.9](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício9.py)

>10. 

Resolução: 

[Resposta Ex.10](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício10.py)

>11. 

Resolução: 

[Resposta Ex.11](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício11.py)

>12. 

Resolução: 

[Resposta Ex.12](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício12.py)

>13. 

Resolução: 

[Resposta Ex.13](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício13.py)

>14. 

Resolução: 

[Resposta Ex.14](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício14.py)















---
## 2.2 Exercícios Python Avançado I

> 

Resolução: 

[Resposta Ex.](./)


---

## 2.3 Exercícios Python Avançado II

> 

Resolução: 

[Resposta Ex.](./)

## 2.4 Exercícios Python ETL

> 

Resolução: 

[Resposta Ex.](./)


--- 

# [Evidências](./Evidencias/)

## 3.1 Exercícios Python Básico

1. Após a execução do código foi gerada uma lista contendo apenas os número ímpares. Conforme podemos ver na imagem a seguir:

![Evidência 1](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício1.png)

2. Após a execução do código foi gerada uma lista no formato pedido fazendo a verificação de cada uma das palavras, se é palíndromo ou não. Conforme podemos ver na imagem a seguir:

![Evidência 2](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício2.png)

3. Após a execução do código, o programa imprimiu o dados na seguinte estrutura pedida: "índice - primeiroNome sobreNome está com idade anos". Conforme podemos ver na imagem a seguir:

![Evidência 3](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício3.png)

4. Foi criada uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Conforme podemos ver na imagem a seguir:

![Evidência 4](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício4.png)

5. Foi realizada a leitura do arquivo person.json, feito o parsing e imprimido seu conteúdo. Conforme podemos ver na imagem a seguir:

![Evidência 5](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício5.png)

6. Implementei a função my_map(list, f) que recebeu uma lista de entrada e aplicou a função de potência de 2 para cada elemento. Conforme podemos ver na imagem a seguir:

![Evidência 6](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício6.png)

7. Foi feito um programa que lê o conteúdo do arquivo texto (arquivo_texto.txt) e imprime o seu conteúdo. Conforme podemos ver na imagem a seguir:

![Evidência 7](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício7.png)

8. Foi criada uma função que recebe um número variável de parâmetros não nomeados, um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido. Conforme podemos ver na imagem a seguir:

![Evidência 8](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício8.png)

---
## 3.2 Exercícios Python Avançado I

1. . Conforme podemos ver na imagem a seguir:

![Evidência 1](./)



---

## 3.3 Exercícios Python Avançado II

1. . Conforme podemos ver na imagem a seguir:

![Evidência 1](./)

---

## 3.4 Exercícios Python ETL

1. . Conforme podemos ver na imagem a seguir:

![Evidência 1](./)


---


# Certificados


Nessa sprint não houve certificados



