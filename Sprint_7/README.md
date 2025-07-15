# 🚀 Sprint 6

## 📌 Resumo

Durante a Sprint 7, continuei aprofundando meus conhecimentos nas ferramentas da AWS para engenharia de dados. Assim, dei continuidade ao desafio final, onde construí a camada Refined do meu Data Lake, aplicando uma modelagem dimensional para facilitar a análise dos dados usando como base o tema escolhido e as perguntas definidas anteriormente nas quais quero responder, criei e alimentei tabelas de dimensão e fato, integrando os dados provenientes da camada Trusted. Utilizei o AWS Glue Studio para desenvolver os jobs e o Glue Data Catalog para registrar as novas estruturas. Por fim, usei o Amazon Athena para validar os resultados.

- **Data & Analytics**: através do D&A obtive as principais informações para seguir com a realização da continuidade do desafio.

- **Modelagem de Dados para Data Warehouse**: Através deste curso, aprendi ainda mais sobre Data Warehouse e modelagem dimensional, compreendendo seus conceitos, objetivos e fatores críticos. Estudei as diferenças entre sistemas OLTP e OLAP, suas aplicações e impactos no desempenho das análises, explorei as principais operações OLAP, como Slice, Dice, Drilling, Ranging e Ranking. Também aprendi a construir um DW, entendendo a importância das tabelas fato e dimensão, além de como estruturá-las com base nos modelos Star Schema e Snowflake, aplicados em ambientes de análise multidimensional.

- **Amazon Q Developer for Programmers and DevOps AWS AI coding**: Por meio deste curso, aprendi a configurar e utilizar o Amazon Q Developer no VSCode e JetBrains, explorando seu uso no chat, geração de código, documentação e testes em Python. Também utilizei a ferramenta para lidar com listas, ambientes virtuais, visualização de dados e integração com GitHub Actions e pull requests. O conteúdo foi direto e prático, com foco na aplicação real da ferramenta no dia a dia do desenvolvimento.

🤔 *Reflexões*


A Sprint 7 foi bastante dinâmica, como alguns conteúdos já vinham sendo trabalhados em sprints anteriores, pude reforçar ainda mais meu conhecimento. Sinto que estou mais adaptada aos desafios e, com o apoio do meu squad e do monitor, consegui superar as dificuldades que surgiram, concluir essa etapa do desafio foi muito gratificante. Sou imensamente grata por todo o suporte que venho recebendo dos monitores, da Scrum Master, do meu time e dos demais membros da PB.



<br>

---

## 🗂️ Sumário 

1. [Desafio](#desafio)

2. [Exercícios](#exercícios)

3. [Certificados](#certificados)

<br>

---

# [Desafio](./Desafio/) 

Nesse desafio, dei continuidade à quarta etapa do projeto final, com foco na construção da camada Refined do Data Lake e na modelagem dimensional dos dados. Criei jobs no AWS Glue Studio para transformar os dados já presentes na camada Trusted, estruturando tabelas de dimensão, ponte e uma tabela fato, essas tabelas foram projetadas para responder às perguntas analíticas definidas previamente, garantindo a integração entre os dados do CSV e da API TMDB.

Após a criação das tabelas no formato Parquet e sua gravação em caminhos organizados no S3, utilizei crawlers para catalogar os dados transformados no Glue Data Catalog dentro do database da camada Refined. Finalizei a sprint com validações no Amazon Athena, verificando a integridade das tabelas, os relacionamentos entre as dimensões e o fato, e confirmando a correta aplicação dos filtros e joins. Os arquivos utilizados para a realização do desafio estão organizados em pastas por etapas, acompanhando as fases do desenvolvimento, e podem ser encontrados na *Pasta Desafio*, as evidências do processo estão armazenadas na *Pasta Evidências* e, para um detalhamento completo do desafio, recomendo consultar o README da pasta *Readme Desafio*. Seguem os links:




- [Pasta Desafio](./Desafio/) 
- [Pasta Evidências](./Evidências/)
- [Readme Desafio](./Desafio/README.md)


<br>

---

# [Exercícios](./Exercícios/)

Na Sprint 7, não houve a realização de exercícios como nas anteriores. O foco principal foi direcionado para o desenvolvimento do desafio final, o que permitiu aplicar, na prática, todos os conhecimentos adquiridos ao longo do programa. Essa etapa foi essencial para consolidar o aprendizado e reforçar minha evolução na trilha.

<br>

---

# Certificados

Durante a Sprint 7, não concluí nenhum curso com certificação da AWS.
