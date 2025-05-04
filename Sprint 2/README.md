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
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Faça um programa que gere uma nova lista contendo apenas números ímpares.

>Resolução: No enunciado é fornecida uma lista e  pedido uma nova lista apenas com números ímpares. Para resolução é necessário percorrer cada elemento da lista a, para fazer iteração utilizei o for, fiz a verificação do número ímpar fazendo o resto da divisão por 2 diferente de 0, por meio do operador módulo (%). Por fim, o append adiciona o número na lista se o resultado da condição for verdadeiro.

[Resposta Ex.1](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício1.py)

<br>
2. Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

> Resolução: Inicialmente criei uma lista com as palavras fornecidas, percorri cada palavra da lista usando o for, adicionei uma condicional para comparar a palavra com sua versão invertida, se fosse verdadeira retornaria palíndromo, senão, retornaria que não é palíndromo.

[Resposta Ex.2](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício2.py)

<br>
3. Dada as listas a seguir:

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".

> Resolução: Antes de começar o código confirmei que todas as listas tinham o mesmo tamanho, após isso iniciei de fato. Para começar, utilizei a função enumerate para percorrer a lista ao mesmo tempo que acessa o índice de cada elemento, toda vez que o for rodar ele irá pegar o índice e cada elemento correspondente ao valor dele nas listas.

[Resposta Ex.3](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício3.py)

<br>
4. Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função:

['abc', 'abc', 'abc', '123', 'abc', '123', '123']

> Resolução: Defini uma função que recebe uma lista como entrada, fiz uso do set para converter a lista em conjunto e eliminar automaticamente os elementos repetidos, depois converti o conjunto novamente em uma lista, retornando a nova lista sem duplicados. Além disso, utilizei docstring para documentação interna da função.

[Resposta Ex.4](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício4.py)

<br>
5. Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

> Resolução: Primeiramente importei o módulo json. Após isso,  usei with open() para abrir e fechar o arquivo automaticamente, a função open possui dois parâmetros obrigatórios: o filename (person.json) e o mode (modo leitura), além desses utilizei utf-8 para garantir que os caracteres especiais fossem lidos corretamente. Por fim, converti o conteúdo do arquivo json em um dicionário python e fiz a exibição.

[Resposta Ex.5](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício5.py)

<br>
6. Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

> Resolução: Criei a função my_map(list, f) na qual  inicia com uma lista vazia para armazenar os resultados, por meio do for é feita a iteração dos elementos da lista aplicando a função em cada um e adicionando o resultado na nova lista. Após isso, passei a lista de entrada e a função que será aplicada em cada elemento, finalizei fazendo a impressão do resultado final

[Resposta Ex.6](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício6.py)

<br>
7. Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

> Resolução: Seguindo a mesma lógica da questão 5, usei with open() para abrir e fechar o arquivo automaticamente, a função open possui dois parâmetros obrigatórios: o filename (arquivo_texto.txt) e o mode (modo leitura), além desses utilizei utf-8 para garantir que os caracteres especiais fossem lidos corretamente. Por fim, fiz a leitura do arquivo como uma string e na função print passei o parâmetro end="" para que a próxima saída seja impressa na mesma linha.

[Resposta Ex.7](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício7.py)

<br>
8. Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido. Teste sua função com os seguintes parâmetros:

(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

> Resolução: Para resolução da questão defini a função valores, que usa o *args para armazenar parâmetros não nomeados e **kwargs para armazenamento de parâmetros nomeados, realizei a iteração sobre o *args por meio do for e fiz o mesmo no **kwargs, porém adicionei o .values() para retornar somente os valores do dicionário e finalizei ambos com a impressão dos valores.

[Resposta Ex.8](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício8.py)

<br>
9. Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

> Resolução: Nesse exercício é necessário criar um molde para representar o estado de uma lâmpada (ligada ou desligada) e as suas ações (ligar e desligar). Assim, defini a classe lâmpada e, no método construtor init, fiz a inicialização dos atributos: o primeiro argumento foi o self, que se refere à instância do objeto, no segundo argumento (ligada:bool) informei que seria um valor booleano (true para ligada e false para desligada), dentro do método, usei self.ligada = ligada para salvar esse valor como o estado atual da lâmpada. Após isso, fiz o método que liga a lâmpada, que desliga e o que verifica se está ligada. Por último, para testar a classe, instanciei um objeto chamado minha_lampada, testei os métodos e imprimi os resultados das verificações.

[Resposta Ex.9](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício9.py)

<br>
10. Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"

> Resolução: Nesse exercício, criei uma função soma_numeros e passei o parâmetro que será fornecido à função (a string com números). Foi criada uma lista na qual separei os números da string usando a vírgula como separador, por meio do método .split(','). No entanto os números ainda estão como string, para fazer a transformação utilizei  list comprehension para transformar cada item em inteiro. Para finalizar a função fiz a soma dos valores da lista, retornando o resultado.

[Resposta Ex.10](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício10.py)

<br>
11. Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

> Resolução: Nesse exercício, criei uma função dividir_lista e passei o parâmetro que será fornecido à função (a lista com números). Utilizei a função len() para obter o tamanho total da lista e, em seguida, dividi esse valor por 3 usando divisão inteira para determinar quantos elementos cada parte da lista deveria conter. Após isso, utilizei a notação de fatiamento para dividir a lista original em três partes iguais. A função retorna essas três partes como uma tupla. Por fim, testei a função com a lista fornecida 

[Resposta Ex.11](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício11.py)

<br>
12. Dado o dicionário a seguir:

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

>Resolução: Inicialmente utilizei o método dicionario.values() para pegar apenas os valores, por meio do set() fiz a remoção de duplicatas e com a função list() converti o conjunto sem duplicatas para formato de lista.

[Resposta Ex.12](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício12.py)

<br>
13. Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada [random_list = random.sample(range(500),50)].


>Resolução: Comecei a questão importando o módulo random do Python. Em seguida, gerei uma lista com 50 números aleatórios entre 0 e 500 por meio da função random.sample(). Depois, ordenei essa lista utilizando a função sorted(). Para realizar os cálculos solicitados, utilizei a função min() para obter o menor valor da lista e max() para o maior. Para calcular a média, usei a fórmula sum()/len() e arredondei o resultado para duas casas decimais com a função round(). No cálculo da mediana, determinei o índice do meio utilizando len() dividido por 2 com divisão inteira (//). Se a quantidade de elementos fosse par, a mediana seria a média dos dois valores centrais, se fosse ímpar, seria o valor central da lista.

[Resposta Ex.13](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício13.py)

<br>
14. Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

>Resolução: Para resolver essa questão, utilizei o fatiamento da lista com passo negativo, para inverter a ordem dos elementos. Após isso, imprimi o resultado da lista invertida.

[Resposta Ex.14](./Exercícios/1.%20Exercícios%20Python%20Básico/Exercício14.py)

<br>

---
## 2.2 Exercícios Python Avançado I

15. Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som. Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo passado.

> Resolução: Criei a classe Passaro com os métodos voar() e emitir_som(), e as classes Pato e Pardal herdaram de Passaro, cada uma implementando sua própria versão do método emitir_som(). Por fim, instanciei objetos de cada classe, chamei os métodos e imprimi as mensagens conforme o enunciado.

[Resposta Ex.15](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Exercício15.py)

<br>
16. Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e um atributo público de nome id. Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.

> Resolução: Comecei a questão criando a classe Pessoa com um construtor que recebe o id como parâmetro. Dentro do construtor, declarei o atributo público id e o atributo privado __nome, inicializado como None. Para garantir o acesso controlado ao atributo privado, utilizei o property. Após isso, criei um método nome decorado com @property, responsável por retornar o valor de __nome, e um método nome decorado com @nome.setter, que define o valor de __nome. Assim, o acesso ao atributo acontece apenas por meio dos métodos definidos, respeitando o encapsulamento. Por fim, instanciei um objeto da classe e testei a atribuição e leitura do nome.

[Resposta Ex.16](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Exercício16.py)

<br>
17. Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

> Resolução: Inicei a questão definindo a classe Calculo, em seguida implementei dois métodos dentro da classe, somando, que recebe dois parâmetros e retorna a soma, e subtraindo, que também recebe dois parâmetros e retorna a subtração. Depois disso, instanciei um objeto da classe e chamei os métodos, passando os valores x = 4 e y = 5. Por fim, armazenei os resultados em variáveis e imprimir as expressões e os resultados no formato solicitado.

[Resposta Ex.17](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Exercício17.py)

<br>
18. Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.

Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.

Imprima o resultado da ordenação crescente e da ordenação decresce.

> Resolução: Comecei a questão criando a classe Ordenadora, que possui o atributo listaBaguncada, passado como parâmetro. Em seguida, defini dois métodos, ordenacaoCrescente, retornando a lista ordenada em ordem crescente usando a função sorted(), e ordenacaoDecrescente, que utiliza o mesmo método com o argumento reverse=True para retornar a lista em ordem decrescente. Depois, instanciei dois objetos da classe (crescente e decrescente) com as listas fornecidas. Por fim, chamei os métodos correspondentes para ordenar as listas e imprimi os resultados no formato solicitado.

[Resposta Ex.18](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Exercício18.py)

<br>
19. Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.

Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.

Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.

Ao final, itere pela lista imprimindo cada um dos objetos no formato do modelo fornecido.

> Resolução: Comecei a questão criando a classe Aviao com os atributos modelo, velocidade_maxima, capacidade e cor, defini o atributo cor como um atributo de instância com valor padrão "Azul". Em seguida, instanciei três objetos da classe Aviao com os valores fornecidos no enunciado e armazenei todos em uma lista chamada avioes. Por fim, percorri essa lista com um laço for e imprimi as informações de cada avião no formato solicitado.

[Resposta Ex.19](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Exercício19.py)

<br>

---

## 2.3 Exercícios Python Avançado II

20.Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes. Você deverá aplicar as seguintes funções no exercício: map, filter, sorted e sum. 

Seu código deverá exibir na saída a lista dos 5 maiores números pares em ordem decrescente e a soma destes valores.

>Abri o arquivo number.txt, li as linhas e fiz a conversão delas em inteiro com a função map. Em seguida, filtrei apenas os números pares por meio da função filter() com uma lambda que retorna true se o número for divisível por 2. Depois, selecionei os cinco maiores usando sorted() em ordem decrescente e fatiamento. Por fim, utilizei print para exibir a lista dos maiores pares e a soma deles usanddo sum().

[Resposta Ex.20](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Exercício20.py)

<br>
21. Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

> Resolução: Utilizei a função filter() com lambda para selecionar apenas as vogais da string, assim, converti cada letra para minúsculo com .lower() antes de verificar se está no conjunto de vogais. Em seguida, transformei essa sequência em uma lista e utilizei len() para contar quantas vogais foram encontradas e retornei esse valor.

[Resposta Ex.21](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Exercício21.py)

<br>
22. A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.

Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução: reduce (módulo functools) e map.

> Resolução: Importei a função reduce do módulo functools para fazer o cálculo dos valores. Em seguida, usei a função map junto com uma lambda para transformar cada lançamento da lista, se o tipo for crédito, o valor vai permanecer positivo, se for débito, o valor é multiplicado por -1, fazendo com que os débitos sejam subtraídos. Após isso, usei reduce para somar todos os valores da lista resultante e retornar o saldo bancário final.

[Resposta Ex.22](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Exercício22.py)

<br>
23. A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.

Na resolução da atividade você deverá aplicar as seguintes funções: max, zip e map

> Resolução: Utilizei a função zip() para combinar os operadores e os operandos. Em seguida, apliquei a função map() junto com uma lambda para executar cada operação sobre os operandos, conforme o operador correspondente. Após isso, utilizei a função max() para retornar o maior valor encontrado entre os resultados. 

[Resposta Ex.23](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Exercício23.py)

<br>
24. Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as informações solicitadas.

O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito.

> Resolução: Primeiramente abri o arquivo em modo leitura e com UTF-8 para garantir a leitura correta dos nomese carreguei as linhas com readlines(). Limpei os dados usando map() com strip() e separei o nome e as notas com split(','). Converti as notas para inteiros e organizei os dados como tuplas, também ordenei os estudantes pelo nome com sorted(). Em seguida, para cada aluno, selecionei as três maiores notas com sorted() e calculei a média com sum() e round(). Para finalizar, imprimi os resultados no formato pedido.

[Resposta Ex.24](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Exercício24.py)

<br>
25. Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado.

O retorno da função obrigatoriamente deve ser uma lista. Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço. 

> Resolução: Primeiramente calculei a média dos preços usando sum() e len() e utilizei filter() com uma função lambda para obter os produtos com preço acima dessa média. Depois apliquei sorted() para ordenar os produtos filtrados com base em seus preços, do menor para o maior. Por fim, pedi para retornar o resultado.

[Resposta Ex.25](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Exercício25.py)

<br>
26. Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início (def pares_ate(n:int):) .

O objetivo da função pares_ate é retornar um generator para os valores pares no intervalo [2,n]. Observe que n representa o valor do parâmetro informado na chamada da função.

> Resolução: Comecei o código usando a função range() para gerar números de 2 até n, com passo 2, apliquei yield para transformar a função em um generator e por meio do for será percorrido apenas os valores desejados.

[Resposta Ex.26](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Exercício26.py)

<br>

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

9. Foi criada uma classe lâmpada,  instanciei o objeto minha_lampada, testei os métodos e imprimi os resultados para verificar se o comportamento. Conforme podemos ver na imagem a seguir:

![Evidência 9](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício9.png)

10. Foi feita uma função que recebe uma string de números separados por vírgulas e retorna a soma de todos eles. Conforme podemos ver na imagem a seguir:

![Evidência 10](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício10.png)

11. Foi feita uma função que  que recebe como parâmetro uma lista e retorna o valor da lista recebida dividida em 3 partes iguais. Conforme podemos ver na imagem a seguir:

![Evidência 11](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício11.png)

12. Foi criada uma lista contendo apenas os valores únicos. Conforme podemos ver na imagem a seguir:

![Evidência 12](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício12.png)

13. Foi calculado o valor mínimo, valor máximo, valor médio e a mediana da lista gerada. Conforme podemos ver na imagem a seguir:

![Evidência 13](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício13.png)

14. A lista fornecida foi impressa de trás para frente. Conforme podemos ver na imagem a seguir:

![Evidência 14](./Exercícios/1.%20Exercícios%20Python%20Básico/Evidências/Exercício14.png)

---
## 3.2 Exercícios Python Avançado I

15. Foram implementadas duas classes, Pato e Pardal , que herdam da superclasse Passaro as habilidades de voar e emitir som e foi imprimido no console os sons de acordo com o modelo. Conforme podemos ver na imagem a seguir:

![Evidência 15](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Evidências/Exercício15.png)

16. Foi criada uma classe chamada Pessoa, com um atributo privado chamado nome e um atributo público de nome id. Adicionado dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo. Por último, o atributo privado pôde ser lido e escrito no modelo informado. Conforme podemos ver na imagem a seguir:

![Evidência 16](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Evidências/Exercício16.png)


17. Criei a classe Calculo, implementei os métodos solicitados dentro da classe (soma e subtração), fiz as operações e imprimi os resultados no formato solicitado. Conforme podemos ver na imagem a seguir:

![Evidência 17](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Evidências/Exercício17.png)

18. Foi criada a classe Ordenadora, que possui o atributo listaBaguncada, defini os métodos de ordenação pedidos e imprimi os resultados no formato solicitado. Conforme podemos ver na imagem a seguir:

![Evidência 18](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Evidências/Exercício18.png)


19. Criei a classe Aviao com os atributos modelo, velocidade_maxima, capacidade e cor e imprimi as informações de cada avião no formato solicitado. Conforme podemos ver na imagem a seguir:

![Evidência 19](./Exercícios/2.%20Exercicios%20Python%20Avançado%20I/Evidências/Exercício19.png)

<br>

---

## 3.3 Exercícios Python Avançado II

20. Abri o arquivo number.txt, utilizei as funções solicitadas para realizar os cálculos (map, filter, sorted e sum) e o código exibiu na saída a lista dos 5 maiores números pares em ordem decrescente e a soma destes valores. Conforme podemos ver na imagem a seguir:

![Evidência 20](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Evidências/Exercício20.png)

21. Fiz a função conta_vogais, na qual o parâmetro de entrada é uma string e o resultado será contagem de vogais presentes em seu conteúdo, também apliquei as funções len(), filter() e lambda para resolução da questão. Conforme podemos ver na imagem a seguir:

![Evidência 21](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Evidências/Exercício21.png)

22. Fiz a função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários, na qual calcula o valor final, somando créditos e subtraindo débitos, utilizando no código as funções lambda, reduce e map. Conforme podemos ver na imagem a seguir:

![Evidência 22](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Evidências/Exercício22.png)

23. Criei a função calcular_valor_maximo na qual recebe dois parâmetros, operadores e operandos, onde aplica cada operação ao respectivo par de operandos e retornar o maior valor dentre eles. Conforme podemos ver na imagem a seguir:

![Evidência 23](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Evidências/Exercício23.png)

24. Fiz a importação do arquivo, a leitura do mesmo, a limpeza dos dados e gerei como saída um relatório em formato textual contendo as informações solicitadas. Conforme podemos ver na imagem a seguir:

![Evidência 24](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Evidências/Exercício24.png)

25. Fiz o cálculo da média dos preços, filtrei os produtos com o valor acima da média e ordenei os produtos filtrados pelo preço (ordem crescente). Conforme podemos ver na imagem a seguir:

![Evidência 25](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Evidências/Exercício25.png)

26. Foi feita a função pares_ate que retorna um generator para os valores pares no intervalo [2,n]. Conforme podemos ver na imagem a seguir:

![Evidência 26](./Exercícios/3.%20Exercicios%20Python%20Avançado%20II/Evidências/Exercício26.png)

<br>

---
## 3.4 Exercícios Python ETL

1. . Conforme podemos ver na imagem a seguir:

![Evidência 1](./)


---


# Certificados


Nessa sprint não houve certificados



