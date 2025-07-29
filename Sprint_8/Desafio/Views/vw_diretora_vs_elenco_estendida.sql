CREATE OR REPLACE VIEW filmes_refined_db.vw_diretora_vs_elenco_estendida AS
WITH direcao AS (
  SELECT fd.id_filme, dd.id_diretor, dd.genero AS genero_diretor
  FROM filmes_refined_db.filmediretor fd
  JOIN filmes_refined_db.dimdiretor dd ON fd.id_diretor = dd.id_diretor
),
elenco_genero AS (
  SELECT
    fa.id_filme,
    da.genero
  FROM filmes_refined_db.filmeartista fa
  JOIN filmes_refined_db.dimartista da ON fa.id_artista = da.id_artista
),
stats AS (
  SELECT
    eg.id_filme,
    d.id_diretor,
    d.genero_diretor,
    SUM(CASE WHEN eg.genero = 1 THEN 1 ELSE 0 END) AS mulheres,
    COUNT(*) AS total_elenco
  FROM elenco_genero eg
  LEFT JOIN direcao d ON eg.id_filme = d.id_filme
  GROUP BY eg.id_filme, d.id_diretor, d.genero_diretor
)
SELECT
  CASE
    WHEN genero_diretor = 1 THEN 'Diretora'
    WHEN genero_diretor = 2 THEN 'Diretor'
    ELSE 'Desconhecido'
  END AS genero_diretor,
  ROUND(AVG(CAST(mulheres AS DOUBLE) / total_elenco), 4) AS media_perc_mulheres, -- decimal entre 0 e 1
  COUNT(DISTINCT id_filme) AS qtd_filmes,
  COUNT(DISTINCT id_diretor) AS qtd_diretores
FROM stats
GROUP BY genero_diretor