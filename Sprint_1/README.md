# 🚀 Sprint 1 

## 📌 Resumo

Durante a Sprint 1, tive meu primeiro contato prático com a metodologia ágil. Apesar de já ter estudado anteriormente, essa foi a primeira vez que pude experienciá-la de fato no dia a dia de um time. Foi uma vivência bastante interessante e dinâmica, que contribuiu muito para o meu entendimento e adaptação ao formato.

No período de onboarding, fui muito bem acolhida pela equipe. Todos se mostraram solícitos, colaborativos e dispostos a ajudar, o que me proporcionou um ambiente seguro para aprender, tirar dúvidas e contribuir. Fiquei especialmente feliz com a abertura para o aprofundamento dos nossos conhecimentos, o incentivo ao compartilhamento de aprendizados e o acesso completo à plataforma Udemy, que nos permitirá expandir ainda mais nossas habilidades técnicas.

Nesta sprint, os principais conteúdos abordados foram:

- **Fundamentos da Segurança da Informação**: pude reforçar conceitos que já conhecia e aprofundar novos aprendizados sobre as diretrizes da Compass, os pilares dos controles de segurança e a classificação de informações por nível de sigilo. Achei interessante como o curso trouxe dilemas reais do dia a dia, o que tornou o conteúdo mais prático e aplicável.
- **Scrum**: revisei os principais conceitos do ciclo Scrum, como papéis, cerimônias e artefatos, e aprofundei o entendimento sobre como aplicar essa metodologia na prática. Achei especialmente interessante por ser algo que já estamos vivenciando no dia a dia da squad, o que ajuda a consolidar o aprendizado. A dinâmica ágil e iterativa do Scrum tem me mostrado o valor da colaboração contínua, da adaptação rápida e da entrega de valor em pequenos ciclos.
- **Git e GitHub**: o formato do curso foi bem dinâmico, com exercícios práticos que ajudaram a fixar os conceitos. Já havia tido contato com Git e GitHub de forma básica anteriormente, e o curso me ajudou a aprofundar alguns pontos, como o uso de branches, commits mais organizados, pull requests e resolução de conflitos. Foi uma ótima oportunidade para reforçar boas práticas no versionamento de código.
- **Markdown**: meu contato anterior com Markdown era bem básico, e o curso me ajudou a entender melhor os conceitos que estou aplicando agora nas entregas das sprints. Aprendi sobre a estruturação de textos, uso de títulos, listas, links, imagens e blocos de código. Foi útil para melhorar a clareza e organização das minhas documentações.
- **SQL**: já tinha estudado SQL de forma bem inicial, mas neste curso pude aprofundar em conceitos mais avançados e reforçar meus conhecimentos. Por meio dos exercícios e desafios propostos na Udemy, consegui aprimorar minha compreensão sobre comandos, operadores, funções, subqueries, tratamento de dados e manipulação de tabelas. Esse aprendizado tem sido essencial para melhorar minha habilidade de trabalhar com bancos de dados de forma mais eficiente e robusta.
- **Modelagem Relacional e Dimensional**: esse foi o último conteúdo abordado antes do desafio. Com links e textos anexados, pude aprofundar meus conhecimentos sobre os tipos de modelagem de banco de dados. Em relação à Modelagem Relacional, foram abordados os conceitos fundamentais, como normalização, chaves primárias e estrangeiras, e a estrutura de tabelas para garantir a integridade dos dados. Já a Modelagem Dimensional foi mencionada com foco na construção de modelos para análise, como o uso de tabelas fato e dimensão. Esse conteúdo me ajudou a entender melhor como aplicar essas modelagens em diferentes cenários de análise de dados.

🤔 *Reflexões*

Esta sprint foi bastante interessante e enriquecedora, pois tive a oportunidade de adquirir uma ampla gama de novos conhecimentos. Apesar de já ter estudado alguns dos conteúdos anteriormente, pude aprofundar e aplicar conceitos importantes na prática. A experiência com a metodologia ágil também foi um grande aprendizado. A parte final da sprint foi um pouco corrida para mim, o que me mostrou a necessidade de aprimorar meu planejamento e priorização de tarefas. No geral, estou bastante animada com o que aprendi até agora e ansiosa para os próximos passos. 

---

## 🗂️ Sumário 

1. [Desafio](#desafio)
2. [Exercícios](#exercícios)
    - [2.1 Exercício Biblioteca](#21-exercicio-biblioteca)
    - [2.2 Exercício Loja](#22-exercicio-loja)
    - [2.3 Exercício Extração de Dados](#23-exercicio-extracao-de-dados)

3. [Evidências](#evidências)
    - [3.1 Exercício Biblioteca](#31-exercicio-biblioteca)
    - [3.2 Exercício Loja](#32-exercicio-loja)
    - [3.3 Exercício Extração de Dados](#33-exercicio-extracao-de-dados)

4. [Certificados](#certificados)

---

# [Desafio](./Desafio/) 

No desafio dessa sprint 1 foi pedido uma normalização da base de dados concessionária e mostrarmos os resultados inicialmente por meio da modelagem relacional. Após isso, utilizando essas tabelas normalizadas, seria necessário realizar uma modelagem dimensional. As evidências do desafio constam em duas pastas: [Desafio](./Desafio/) e  [Evidencias](./Evidencias/). Na qual a primeira concentra-se o arquivo do banco de dados, os diagramas e os arquivos sql, a segunda possui as evidências das imagens.

Esse desafio foi bastante interessante, pude realmente me "desafiar" foi a primeira vez que tive um contato com essa estrutura e formato, foram dias de muito pensamento e "quebrando a cabeça", mas vi um crescimento incrível de conhecimentos adquiridos, minhas squad me ajudou bastante para chegar até essa solução final. Ansiosa para os próximos!

[Readme Desafio](./Desafio/README.md)

---

# [Exercícios](./Exercícios/)

## 2.1 Exercício Biblioteca

>1. Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas. Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.

Resolução: Para resolver este exercício, iniciei explorando a estrutura da tabela livro com um SELECT *, a fim de compreender os dados disponíveis. Como o enunciado solicita todas as colunas da tabela, optei por manter o SELECT *, o que garante que todos os campos esperados sejam retornados. A filtragem foi feita com base na data de publicação, utilizando o operador > para retornar apenas os livros publicados após 2014. A ordenação foi aplicada sobre a coluna cod, conforme solicitado, em ordem crescente.

[Resposta Ex.1](./Exercícios/1.%20Exercício%20Biblioteca/exercício1.sql)

>2. Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente. Atenção às colunas esperadas no resultado final:  titulo, valor.

Resolução: A abordagem começou com a seleção apenas das colunas requeridas pelo enunciado: titulo e valor, da tabela livros. Em seguida, foi aplicada uma ordenação decrescente pela coluna valor, para que os livros com os maiores preços fossem apresentados primeiro. Por fim, utilizei a cláusula LIMIT 10 para restringir o resultado aos 10 livros mais caros, conforme solicitado.

[Resposta Ex.2](./Exercícios/1.%20Exercício%20Biblioteca/exercício2.sql)

> 3. Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

Resolução: Para resolver esse exercício, utilizei a função COUNT() sobre a coluna cod da tabela livro para calcular a quantidade de livros associados a cada editora. Em seguida, selecionei os campos adicionais requeridos: o nome da editora, bem como estado e cidade, provenientes da tabela de endereco. As tabelas foram relacionadas utilizando JOIN, conectando os livros à editora e a editora ao endereço. A cláusula GROUP BY foi aplicada com base na identificação da editora, permitindo a contagem por grupo. Por fim, os resultados foram ordenados de forma decrescente pela quantidade de livros e limitados aos 5 primeiros registros.

[Resposta Ex.3](./Exercícios/1.%20Exercício%20Biblioteca/exercício3.sql)

> 4. Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

Resolução:A construção da query teve início a partir da tabela autor, pois o objetivo era relacionar os autores com os livros de sua autoria. Utilizei um JOIN para conectar a tabela autor à tabela livro, função COUNT() foi aplicada para contar quantos livros cada autor publicou. Em seguida, os dados foram agrupados com GROUP BY com base no codautor, garantindo a contagem correta por autor. Por fim, ordenei os resultados de forma crescente pelo nome do autor, conforme especificado no enunciado.

[Resposta Ex.4](./Exercícios/1.%20Exercício%20Biblioteca/exercício4.sql)

> 5. Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

Resolução: A query foi construída a partir da tabela autor, realizando um JOIN com a tabela livro para identificar os livros escritos por cada autor. Em seguida, conectei a tabela editora, responsável pela publicação dos livros, e, por fim, a tabela endereco, que contém a localização das editoras. A cláusula WHERE foi utilizada para filtrar os registros de editoras fora da região sul do Brasil, excluindo os estados Paraná, Santa Catarina e Rio Grande do Sul. A cláusula DISTINCT foi aplicada para garantir que o nome de cada autor apareça apenas uma vez no resultado. Por fim, os dados foram ordenados em ordem crescente pelo nome do autor.

[Resposta Ex.5](./Exercícios/1.%20Exercício%20Biblioteca/exercício5.sql)

> 6. Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

Resolução: Nesta query, foi utilizada a função COUNT() para calcular a quantidade de livros publicados por cada autor, nomeando esse resultado como quantidade_publicacoes. A consulta foi iniciada a partir da tabela autor, que é unida à tabela livro por meio do JOIN. A cláusula GROUP BY foi utilizada para agrupar os dados por autor, permitindo a contagem correta das publicações por autor. Em seguida, a ordenação foi feita de forma decrescente pela quantidade de publicações, e a cláusula LIMIT 1 foi usada para retornar apenas o autor com maior número de livros publicados.

[Resposta Ex.6](./Exercícios/1.%20Exercício%20Biblioteca/exercício6.sql)

> 7. Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

Resolução: A consulta foi construída a partir da tabela autor, utilizando um LEFT JOIN com a tabela livro para manter todos os autores na listagem, mesmo aqueles que não possuem livros associados. Esse tipo de junção permite identificar os autores sem publicações, já que os campos da tabela livro aparecerão como NULL nesses casos. Para filtrar apenas os autores sem livros, foi aplicada a cláusula WHERE livro.cod IS NULL. Por fim, os nomes foram ordenados em ordem crescente conforme solicitado.

[Resposta Ex.7](./Exercícios/1.%20Exercício%20Biblioteca/exercício7.sql)


---
## 2.2 Exercício Loja

> 8. Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

Resolução: A solução foi elaborada com o uso de uma subquery, apelidada de v. Dentro dessa subquery, utilizei a TBVENDAS e apliquei o filtro WHERE status = 'Concluído' para considerar apenas as vendas finalizadas. Em seguida,  agrupei pelo código do vendedor, fiz a contagem de linhas (vendas de cada vendedor) por meio do COUNT(*), ordenei os vendedores pelo total_vendas do maior para o menor e limitei a 1 para que retornasse o que mais vendeu. Por meio do JOIN fiz a junção das duas tabelas: TBVENDEDOR de alias 'vdd' com a subquery 'v' para conseguirmos o nome do vendedor que mais vendeu. No SELECT, foram retornadas apenas as colunas cdvdd e nmvdd, conforme solicitado.

[Resposta Ex.8](./Exercícios/2.%20Exercicio%20Loja/exercício8.sql)

> 9. Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

Resolução: A estratégia adotada foi iniciar com uma subquery (p) que consulta a tabela TBVENDAS. Dentro dela, apliquei dois filtros principais: o primeiro para selecionar apenas as vendas com o status 'Concluído', e o segundo utilizando a cláusula BETWEEN para limitar as vendas ao intervalo entre 2014-02-03 e 2018-02-02. Após aplicar os filtros, agrupei os resultados pelo código e nome do produto e utilizei a função SUM(qtd) para calcular o total de unidades vendidas por produto.
Em seguida, os dados foram ordenados de forma decrescente para destacar o produto mais vendido, e o LIMIT 1 garantiu que apenas esse produto fosse retornado. A query externa apenas seleciona as colunas necessárias da subquery.

[Resposta Ex.9](./Exercícios/2.%20Exercicio%20Loja/exercício9.sql)

> 10. A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído. As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

Resolução: Para resolver o exercício, foi feita a junção da tabela de vendas com a de vendedores. Em seguida, apliquei o filtro para considerar apenas as vendas com status “Concluído”. No SELECT, calculei o valor total vendido por cada vendedor multiplicando a quantidade pelo valor unitário e somando os resultados. A comissão foi calculada multiplicando esse total pelo percentual de comissão, convertido para decimal. Ambos os valores foram arredondados para duas casas decimais com a função ROUND. Por fim, agrupei os dados por vendedor e ordenei os resultados pela comissão em ordem decrescente.

[Resposta Ex.10](./Exercícios/2.%20Exercicio%20Loja/exercício10.sql)

> 11. Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

Resolução: A consulta foi feita sobre a tabela de vendas, filtrando apenas os registros com status "Concluído". No SELECT, foram selecionados o código, o nome do cliente e o gasto total, calculado multiplicando a quantidade pelo valor unitário de cada venda e somando os resultados. O valor foi arredondado para duas casas decimais com ROUND. A agregação foi feita por cliente e os resultados ordenados do maior para o menor gasto, com o LIMIT 1 retornando apenas o cliente que mais gastou.

[Resposta Ex.11](./Exercícios/2.%20Exercicio%20Loja/exercício11.sql)

> 12. Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas. Observação: Apenas vendas com status concluído.

Resolução: Utilizei a cláusula WITH para criar a subconsulta TotalVendas, que calcula o total bruto de vendas por vendedor, considerando apenas vendas com status "Concluído" e eliminando aqueles com total zero usando o HAVING. Em seguida, criei a subconsulta VendedorMenorVenda para identificar o vendedor com menor valor total de vendas. No SELECT principal, juntei essa informação com a tabela de dependentes para retornar os dados dos dependentes vinculados ao vendedor com menor faturamento.

[Resposta Ex.12](./Exercícios/2.%20Exercicio%20Loja/exercício12.sql)

> 13. Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas). As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

Resolução: No SELECT, defini as colunas desejadas e calculei o total de vendas por produto e canal usando SUM(qtd). Filtrei os dados considerando apenas vendas concluídas com os canais "Ecommerce" ou "Matriz", agrupando os resultados por produto e canal. Por fim, ordenei pela soma das quantidades vendidas em ordem crescente e limitei a 10 registros para obter os menos vendidos.

[Resposta Ex.13](./Exercícios/2.%20Exercicio%20Loja/exercício13.sql)

> 14. Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente. Observação: Apenas vendas com status concluído.

Resolução: No SELECT informei as colunas que deveriam me retornar os resultados: a do nome do estado e o de gastomedio, na qual realizei o cálculo do  valor bruto de cada venda (qtd * vrunt) e a média desse valor arredondando para 2 casas decimais. Por meio da TBVENDAS realizei o filtro  dos registros para considerar apenas as vendas que foram concluídas, agrupei os dados por estado, para saber o gasto médio por estado e ordenei  o resultado de forma decrescente para mostrar primeiro os estados com maior gasto médio.

[Resposta Ex.14](./Exercícios/2.%20Exercicio%20Loja/exercício14.sql)

> 15. Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

Resolução: Utilizei a tabela TBVENDAS e filtrei as vendas com a coluna deletado igual a 1, que indica que foram deletadas. No SELECT retornei apenas o código da venda e ordenei o resultado de forma crescente.

[Resposta Ex.15](./Exercícios/2.%20Exercicio%20Loja/exercício15.sql)

> 16. Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º). Obs: Somente vendas concluídas.

Resolução: Utilizei a tabela TBVENDAS e apliquei o filtro WHERE para considerar apenas vendas concluídas. No SELECT, retornei as colunas de estado, nome do produto e a média de quantidade vendida, arredondada para quatro casas decimais. Agrupei os dados por estado e produto, e ordenei o resultado primeiro pelo nome do estado e depois pelo nome do produto.

[Resposta Ex.16](./Exercícios/2.%20Exercicio%20Loja/exercício16.sql)


---

## 2.3 Exercício Extração de Dados

> 1. Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar o caractere ";" (ponto e vírgula) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo: CodLivro Titulo CodAutor NomeAutor Valor CodEditora NomeEditora

Resolução: No SELECT, defini as colunas com alias para corresponder aos nomes exigidos no arquivo CSV. Utilizei dois LEFT JOIN, um para associar a tabela de autores e outro para a de editoras. A ordenação foi feita com base no valor do livro em ordem decrescente, retornando os 10 livros mais caros com o LIMIT 10.

[Etapa 1 - CSV](./Exercícios/3.%20Exercício%20Extração%20de%20Dados/etapa_1.csv)

[Etapa 1 - SQL](./Exercícios/3.%20Exercício%20Extração%20de%20Dados/etapa1.sql)

> 2. Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. Utilizar o caractere "|" (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nome de cabeçalho que listamos abaixo: CodEditora NometEditora QuantidadeLivros

Resolução: Utilizei SELECT com alias para os nomes exigidos no CSV. Após isso, fiz um LEFT JOIN entre editora e livro e usei COUNT para contar os livros por editora, agrupei com GROUP BY, ordenei por quantidade de livros em ordem decrescente e limitei o resultado aos 5 primeiros com LIMIT 5.

[Etapa 2 - CSV](./Exercícios/3.%20Exercício%20Extração%20de%20Dados/etapa_2.csv)

[Etapa 2 - SQL](./Exercícios/3.%20Exercício%20Extração%20de%20Dados/etapa2.sql)



# [Evidências](./Evidencias/)

## 3.1 Exercício Biblioteca

1. A execução da query retornou com sucesso todos os registros de livros cuja data de publicação é posterior a 31 de dezembro de 2014. Os dados foram apresentados ordenadamente pela coluna cod, e todas as colunas solicitadas estavam presentes no resultado, validando a correção da abordagem. Conforme podemos ver na imagem a seguir:

![Evidência 1](./Exercícios/1.%20Exercício%20Biblioteca/Evidências/exercício1.png)

2. A consulta retornou corretamente os 10 livros com os maiores valores cadastrados na tabela livro, ordenados do mais caro ao mais barato. O resultado exibiu exclusivamente as colunas titulo e valor, conforme especificado no enunciado, atendendo a todos os critérios do exercício. Conforme podemos ver na imagem a seguir:

![Evidência 2](./Exercícios/1.%20Exercício%20Biblioteca/Evidências/exercício2.png)


3. A query retornou com sucesso as 5 editoras com maior número de livros cadastrados na biblioteca, exibindo a contagem de livros (quantidade), o nome da editora, e sua respectiva localização (estado e cidade). A ordenação decrescente destacou as editoras mais representativas em termos de volume de publicações, atendendo a todos os critérios definidos no enunciado. Conforme podemos ver na imagem a seguir:

![Evidência 3](./Exercícios/1.%20Exercício%20Biblioteca/Evidências/exercício3.png)


4. Nesse exercício consulta não retornou o esperado, o resultado obtido foi a quantidade de livros publicada por cada autor, exibindo também o código (codautor), o nome e a data de nascimento de cada um. Os dados foram apresentados em ordem alfabética crescente pelo nome do autor, facilitando a leitura e análise. No entanto, a minha resolução não coincidiu com os valores que deveriam retornar para obtenção de sucesso do exercício. Conforme podemos ver na imagem a seguir:

![Evidência 4](./Exercícios/1.%20Exercício%20Biblioteca/Evidências/exercício4.png)



5. A consulta retornou corretamente a lista de autores que tiveram livros publicados por editoras localizadas fora da região sul, sem repetições de nomes e com a ordenação alfabética conforme solicitado. O uso de DISTINCT foi essencial para garantir a unicidade dos nomes no resultado, atendendo a todos os requisitos do exercício. Conforme podemos ver na imagem a seguir:

![Evidência 5](./Exercícios/1.%20Exercício%20Biblioteca/Evidências/exercício5.png)



6. A execução da query retornou corretamente o autor com o maior número de livros cadastrados na base de dados. O resultado exibiu as colunas codautor, nome e quantidade_publicacoes, conforme exigido no enunciado. O uso das funções de agregação e ordenação permitiu identificar o autor com maior número de livros publicados. Conforme podemos ver na imagem a seguir:

![Evidência 6](./Exercícios/1.%20Exercício%20Biblioteca/Evidências/exercício6.png)


7. A execução da query retornou corretamente os nomes dos autores que ainda não possuem nenhum livro publicado na base de dados. Os resultados vieram organizados em ordem alfabética, e a lógica de uso do LEFT JOIN com verificação de NULL garantiu a exatidão do filtro. A solução atendeu integralmente aos critérios estabelecidos no exercício. Conforme podemos ver na imagem a seguir:

![Evidência 7](./Exercícios/1.%20Exercício%20Biblioteca/Evidências/exercício7.png)


---

## 3.2 Exercício Loja

8. A query retornou com precisão o código e o nome do vendedor que mais realizou vendas com status concluído. A utilização de subquery e agregação garantiu que o resultado fosse restrito ao vendedor mais eficiente em termos de número de vendas finalizadas, respeitando todos os requisitos propostos no enunciado. Conforme podemos ver na imagem a seguir:

![Evidência 8](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício8.png)


9. A consulta retornou corretamente o produto mais vendido (em quantidade de unidades) dentro do intervalo de tempo especificado e com o status de venda concluído. As colunas cdpro e nmpro foram apresentadas conforme exigido, garantindo clareza e foco no produto de maior saída nesse período. Conforme podemos ver na imagem a seguir:

![Evidência 9](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício9.png)


10. A query retornou com precisão a lista de todos os vendedores que realizaram vendas concluídas, apresentando o valor total vendido e a comissão individual, ambos arredondados corretamente. A ordenação por comissão permitiu uma visualização clara do desempenho dos vendedores segundo o critério de ganho com comissões, cumprindo integralmente as exigências do exercício. Conforme podemos ver na imagem a seguir:

![Evidência 10](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício10.png)


11. A query retornou corretamente o cliente que mais gastou na loja, considerando apenas vendas concluídas. O valor final foi apresentado com precisão e no formato exigido, evidenciando o cliente de maior impacto financeiro para o negócio. Conforme podemos ver na imagem a seguir:

![Evidência 11](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício11.png)


12. A query retornou corretamente os dados dos dependentes do vendedor que teve o menor valor bruto em vendas concluídas. O uso de CTEs facilitou a estrutura e clareza da lógica, garantindo um resultado eficiente e bem filtrado. Conforme podemos ver na imagem a seguir:

![Evidência 12](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício12.png)


13. A query retornou corretamente os 10 produtos com menor volume de vendas nos canais especificados, atendendo ao filtro de status e organização dos dados conforme solicitado.. Conforme podemos ver na imagem a seguir:

![Evidência 13](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício13.png)


14. A query retorna corretamente os estados com seus respectivos gastos médios, em ordem decrescente, atendendo aos critérios estabelecidos no enunciado. Conforme podemos ver na imagem a seguir:

![Evidência 14](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício14.png)


15. A query retorna corretamente os códigos das vendas deletadas, em ordem crescente. Conforme podemos ver na imagem a seguir:

![Evidência 15](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício15.png)


16. A query retorna corretamente a quantidade média vendida por produto em cada estado, respeitando o ordenamento e o arredondamento exigido. Conforme podemos ver na imagem a seguir:

![Evidência 16](./Exercícios/2.%20Exercicio%20Loja/Evidências/exercício16.png)


---

## 2.3 Exercício Extração de Dados

Etapa 1. A query retornou corretamente os 10 livros com os maiores valores cadastrados na base, incluindo informações completas do autor e da editora. A estrutura está adequada para exportação em formato CSV com separador ; conforme solicitado.

![Evidência - Etapa 1](./Exercícios/3.%20Exercício%20Extração%20de%20Dados/Evidências/etapa1.png)

Etapa 2. A query retornou corretamente as 5 editoras com o maior número de livros registrados na base, incluindo seus respectivos códigos, nomes e quantidade total de publicações. A estrutura do resultado está pronta para exportação em formato CSV com separador pipe, conforme especificado.

![Evidência - Etapa 2](./Exercícios/3.%20Exercício%20Extração%20de%20Dados/Evidências/etapa2.png)


---


# Certificados


Nessa sprint não houve certificados



