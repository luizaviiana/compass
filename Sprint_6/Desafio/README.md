# 🚀 Desafio 

## 📌 Resumo

Nesse desafio dei continuidade à terceira etapa do projeto, o foco foi o processamento e organização dos dados na camada Trusted do Data Lake, utilizando o serviço AWS Glue para transformar os arquivos da camada Raw. Para isso, criei dois jobs em Glue, um para processar os arquivos CSV e outro para os dados da API TMDB no formato JSON, convertendo-os para o formato Parquet e organizando-os conforme o padrão de estrutura definido para o projeto.

Em seguida, configurei e executei crawlers para catalogar esses dados na camada Trusted, garantindo a criação das tabelas no Glue Data Catalog dentro do database dedicado ao projeto. Finalizei a etapa com a validação dos dados via AWS Athena, conferindo a existência das tabelas e a possibilidade de consultas SQL para suportar análises futuras. Essa etapa consolidou a organização da camada Trusted, facilitando o acesso e a consulta dos dados de forma eficiente e padronizada, além de preparar a base para os próximos passos do projeto.


## 🗂️ Sumário 

1. [Etapa 3](#etapa-3)

<br>

---

# Etapa 3

A seguir estarei detalhando um pouco mais dos scripts utilizados em cada etapa, de como foi a execução e as evidências de cada ação tomada:

| Arquivo | Link |
|--------|------|
| glue_job_csv | [🔗 glue_job_csv ](./glue_job_csv.py) |
| glue_job_tmdb | [🔗 glue_job_tmdb ](./glue_job_tmdb.py) |
<br>

> Explicação 

**Data Catalog**

Para o desafio, iniciei criando o Glue Database com o nome filmes_trusted_db, esse banco de dados servirá como catálogo central para registrar as tabelas da camada Trusted, permitindo que os dados processados pelos jobs do AWS Glue fiquem acessíveis via AWS Athena para futuras análises.

![Evidência 1](../Evidências/evidencia1.png)

**Job + Crawler para CSV**

Para dar continuidade ao processamento dos dados CSV, criei um job no AWS Glue com o nome job_process_movies_csv, utilizando a role AWSGlueServiceRole-Lab4 com permissões de leitura e escrita no bucket. Mantive o tipo Spark, com Glue Version 3.0 e linguagem Python 3. Configurei o job com o worker type G 1x, com escalonamento automático desativado e número fixo de 2 workers. Também defini o número de tentativas como 0 e um tempo limite de execução de 5 minutos. 

![Evidência 2](../Evidências/evidencia2.png)

Para esse job, desenvolvi um script Python para o AWS Glue Job com o objetivo de processar o arquivo movies.csv localizado na camada Raw do S3. O script inicializa o contexto do Glue e do Spark, define o caminho de origem para o arquivo CSV e realiza sua leitura utilizando o separador pipe, para facilitar o monitoramento, incluí prints que exibem o total de linhas lidas e o caminho onde os dados serão gravados. O DataFrame resultante é então gravado em formato Parquet na camada Trusted do S3, seguindo a estrutura definida em s3://data-compass-ana/Trusted/Local/Parquet/Movies/. Como que não era necessário realizar tratamento nesta etapa, apenas converti o DataFrame original para o formato Parquet, e utilizei o modo overwrite para garantir que execuções subsequentes substituam os dados anteriores, o job é finalizado com o comando job.commit() para registrar o término da execução.

![Evidência 3](../Evidências/evidencia3.png)

![Evidência 4](../Evidências/evidencia4.png)

Para a etapa de catalogação dos dados processados, criei um Glue Crawler chamado crawler_movies_csv. Utilizei a role de execução AWSGlueServiceRole-Lab4, que possui as permissões necessárias para acessar os dados no bucket S3 e atualizar o Glue Data Catalog. Configurei o crawler para apontar para o caminho do S3 onde os arquivos Parquet do arquivo movies.csv foram gravados, ou seja, s3://data-compass-ana/Trusted/Local/Parquet/Movies/. Os metadados extraídos pelo crawler foram catalogados no database filmes_trusted_db, que foi criado previamente para centralizar o catálogo do projeto. Dessa forma, os dados ficam organizados e acessíveis para consultas futuras via Athena.

![Evidência 5](../Evidências/evidencia5.png)



**Job + Crawler para TMDB**

Nessa parte, segui com o processamento dos dados da API TMDB, onde criei um job no Glue com o nome job_process_tmdb_json, utilizando a role AWSGlueServiceRole-Lab4, segui com as mesmas configurações que já tinha realizado anteriormente: Glue Version 3.0, linguagem Python 3, worker type G 1x, escalonamento automático desativado, número fixo de 2 workers, número de tentativas como 0 e um tempo limite de execução de 5 minutos.

![Evidência 6](../Evidências/evidencia6.png)

Depois, fiz um script para processar os arquivos JSON da API TMDB na camada Raw do S3, definindo manualmente o schema completo dos dados para garantir que todas as estruturas complexas, como arrays e objetos aninhados, fossem corretamente interpretadas. Inicializei os contextos do Glue e Spark, e realizei a leitura dos arquivos JSON usando as opções multiline=True e recursiveFileLookup=True para capturar todos os arquivos do diretório. Para organizar melhor a saída, extraí automaticamente o ano, mês e dia do caminho de origem para construir dinamicamente o caminho de destino na camada Trusted. Em seguida, gravei os dados no formato Parquet, no caminho Trusted/TMDB/Parquet/Movies/{ano}/{mes}/{dia}/, utilizando o modo overwrite para garantir a atualização dos dados. Finalizei o job com job.commit(). Essa abordagem garantiu a padronização da estrutura dos dados e facilitou consultas futuras no Athena, evitando problemas de inconsistência e erros relacionados ao schema.

![Evidência 7](../Evidências/evidencia7.png)

![Evidência 8](../Evidências/evidencia8.png)

Para disponibilizar os dados processados da API TMDB no Glue Data Catalog, criei o crawler com o nome crawler_movies_tmdb. Configurei como fonte de dados o caminho s3 correspondente, que contém os arquivos Parquet gerados a partir dos arquivos JSON da camada Raw. Utilizei a IAM Role AWSGlueServiceRole-Lab4, com as permissões necessárias de leitura no S3 e acesso ao Glue. Apontei como destino o banco de dados filmes_trusted_db, previamente criado, permitindo que o Glue crie e atualize automaticamente a tabela conforme os dados encontrados. Após a criação, executei o crawler para que a tabela correspondente fosse criada no catálogo e pudesse ser consultada posteriormente via AWS Athena.

![Evidência 9](../Evidências/evidencia9.png)

**Exploração e validação no Athena**

Para concluir a preparação da camada Trusted, executei os dois crawlers previamente criados no AWS Glue: crawler_movies_csv e crawler_movies_tmdb. Ambos estavam configurados para escanear os diretórios Trusted correspondentes aos dados do CSV e da API TMDB, e atualizar o catálogo de dados no database filmes_trusted_db. Após a execução bem-sucedida, acessei o AWS Athena e confirmei a criação automática das tabelas csv_movies e tmdb_movies, que representam os dados já convertidos para o formato Parquet e prontos para consultas SQL. Com isso, finalizei a organização e catalogação dos dados da camada Trusted, deixando o ambiente pronto para análise via Athena.

![Evidência 10](../Evidências/evidencia10.png)

![Evidência 11](../Evidências/evidencia11.png)