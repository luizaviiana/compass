# 🚀 Sprint 6

## 📌 Resumo



- **Data & Analytics**: através do D&A, pude ...... . Além disso, também forneceu as principais informações para seguir com a realização dos exercícios e do desafio.

- **AWS - Tutoriais Técnicos - Analytics**: 

- **Fundamentals of Analytics on AWS – Part 2 (Português)**: Neste curso, aprofundei meus conhecimentos sobre data lakes, data warehouses e arquiteturas de dados modernas na AWS, complementando os conceitos da Parte 1. Aprendi como serviços como AWS Lake Formation, Amazon Redshift, Amazon S3, AWS Glue e Amazon Athena são usados para projetar soluções escaláveis de análise de dados.

- **AWS Glue Getting Started (Português)**: Por meio desse curso, adquiri conhecimentos práticos sobre o AWS Glue, o serviço de integração de dados serverless da AWS para ETL. Aprendi como ele simplifica a preparação, catalogação e transformação de dados para análises, machine learning e desenvolvimento de aplicações.

🤔 *Reflexões*




<br>

---

## 🗂️ Sumário 

1. [Desafio](#desafio)

2. [Exercícios](#exercícios)
    - 2.1 [Geração e massa de dados](#21-geração-e-massa-de-dados)
    - 2.2 [Apache Spark](#)
    - 2.3 [Lab AWS Glue](#)

3. [Certificados](#certificados)

<br>

---

# [Desafio](./Desafio/) 

. Os arquivos utilizados para a realização do desafio estão organizados em pastas por etapas, acompanhando as fases do desenvolvimento, e podem ser encontrados na *Pasta Desafio*. As evidências do processo estão armazenadas na *Pasta Evidências*. Para um detalhamento completo do desafio, recomendo consultar o README da pasta *Readme Desafio*. Seguem os links:

- [Pasta Desafio](./Desafio/) 
- [Pasta Evidências](./Evidências/)
- [Readme Desafio](./Desafio/README.md)


<br>

---

# [Exercícios](./Exercícios/)

## 2.1 Geração e massa de dados

Neste exercício, a proposta foi gerar dados em Python que serão utilizados futuramente em atividades com o framework Apache Spark. O exercício foi dividido em três etapas, todas voltadas à manipulação de listas e geração de arquivos, com foco em aquecer o uso da linguagem Python antes de processamentos mais pesados com Spark. Para a execução, utilizei o Jupyter Notebook para desenvolver e validar as etapas 1, 2 e o teste da etapa 3, aproveitando a visualização interativa do ambiente. Já a etapa 3 completa, que envolve a geração de 10 milhões de nomes, foi implementada em um script Python separado (Etapa3.py) e executada via terminal, garantindo maior performance no processamento e gravação dos dados. Abaixo, detalho os passos realizados em cada etapa, os códigos utilizados e as decisões técnicas adotadas.

| Arquivo | Link |
|--------|------|
| Exercício1.ipynb | [🔗 Exercício1.ipynb](./Exercícios/Exercício1/Exercício1.ipynb) |
| Etapa3.py | [🔗 Etapa3.py](./Exercícios/Exercício1/Etapa3.py) |
<br>

>Resolução:

Etapa 1 – Utilizei a biblioteca random para gerar uma lista contendo 250 números inteiros aleatórios entre 1 e 1000. Em seguida, apliquei o método .reverse() para inverter a ordem dos elementos dessa lista. Para finalizar, imprimi o resultado para validação.

![Evidência 1](./Exercícios/Exercício1/Evidências/Evidencia1.png)

Etapa 2 – Na segunda etapa, ainda utilizando o Jupyter Notebook, declarei manualmente uma lista contendo 20 nomes de animais. Em seguida, utilizei o método .sort() para ordená-los em ordem alfabética e imprimi cada item individualmente utilizando list comprehension. Por fim, salvei o conteúdo da lista em um arquivo de texto chamado animais_ordenados.txt, com um animal por linha, utilizando o comando with open() para abrir e escrever o arquivo de forma eficiente.

| Arquivo | Link |
|--------|------|
| animais_ordenados.txt | [🔗 animais_ordenados.txt](./Exercícios/Exercício1/animais_ordenados.txt) |
<br>

![Evidência 2](./Exercícios/Exercício1/Evidências/Evidencia2.png)

Etapa 3 – Para validar a lógica antes de rodar a versão completa da terceira etapa, iniciei com uma versão reduzida no Jupyter Notebook. Instalei a biblioteca names através do terminal com o comando pip install names, e em seguida utilizei essa biblioteca para gerar 1.000 nomes únicos. A partir dessa base, gerei uma lista com 10 mil nomes aleatórios usando random.choice() e salvei os dados em um arquivo chamado nomes_aleatorios_teste.txt, com um nome por linha. Esse teste me permitiu garantir que toda a lógica de geração e gravação estava funcionando corretamente, antes de executar o processo completo no terminal.

| Arquivo | Link |
|--------|------|
| nomes_aleatorios_teste.txt | [🔗 nomes_aleatorios_teste.txt](./Exercícios/Exercício1/nomes_aleatorios_teste.txt) |
<br>

![Evidência 3](./Exercícios/Exercício1/Evidências/Evidencia3.png)
<br>

Após validar a lógica da geração de nomes com a versão de teste no Jupyter Notebook, desenvolvi a versão final da terceira etapa em um script separado chamado Etapa3.py. Neste script, utilizei a biblioteca names para gerar 39.080 nomes únicos e, a partir dessa base, criei 10 milhões de nomes aleatórios com a função random.choice(). Para garantir performance na escrita, abri o arquivo nomes_aleatorios.txt uma única vez utilizando o comando with open(), gravando todos os nomes de forma sequencial, um por linha. Executei esse script diretamente no terminal com o comando python Etapa3.py, o que permitiu melhor desempenho no processamento e na geração do arquivo final.

| Arquivo | Link |
|--------|------|
| nomes_aleatorios.txt | [🔗 nomes_aleatorios.txt](./Exercícios/Exercício1/nomes_aleatorios.txt) |
<br>

![Evidência 4](./Exercícios/Exercício1/Evidências/Evidencia4.png)

<br>

## 2.2 Apache Spark







<br>

---


# Certificados


Durante essa sprint, concluí os cursos AWS: Fundamentals of Analytics on AWS – Part 2 (Português) e AWS Glue Getting Started (Português). A seguir, compartilho os certificados correspondentes:

| Certificado | Link |
|--------|------|
| Fundamentals of Analytics on AWS – Part 2 (Português) | [🔗 Link ](./Certificados/Fundamentals%20of%20Analytics%20on%20AWS%20–%20Part%202%20(Português).pdf) |
| AWS Glue Getting Started (Português) | [🔗 Link ](./Certificados/AWS%20Glue%20Getting%20Started%20(Português).pdf) |
<br>
