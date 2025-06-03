/* Criando o banco de dados */
CREATE DATABASE meubanco

/* Query para criar a tabela no banco de dados que criei */
CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.nomes (
  nome STRING,
  sexo STRING,
  total INT,
  ano INT
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
)
LOCATION 's3://ana-luiza-static-site/dados/'
TBLPROPERTIES ('skip.header.line.count' = '1')

/*Consulta os 15 nomes mais utilizados no ano de 1999 */
SELECT nome FROM meubanco.nomes 
WHERE ano = 1999 ORDER BY total DESC LIMIT 15


/*Consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje */
WITH ranked_names AS (
  SELECT 
    decada,
    nome,
    total,
    ROW_NUMBER() OVER (PARTITION BY decada ORDER BY total DESC) AS posicao
  FROM (
    SELECT 
      nome,
      FLOOR(ano / 10) * 10 AS decada,
      SUM(total) AS total
    FROM meubanco.nomes
    WHERE ano >= 1950
    GROUP BY nome, FLOOR(ano / 10) * 10
  ) AS sub
)
SELECT decada, nome, total
FROM ranked_names
WHERE posicao <= 3
ORDER BY decada, posicao