CREATE OR REPLACE VIEW filmes_refined_db.vw_diretores_com_mais_representatividade AS
WITH elenco_genero AS (
  SELECT
    fa.id_filme,
    da.genero
  FROM filmes_refined_db.filmeartista fa
  JOIN filmes_refined_db.dimartista da ON fa.id_artista = da.id_artista
  WHERE fa.id_filme IN (SELECT id_filme FROM filmes_refined_db.fatorepresentacaofeminina)
),
perc_mulheres_por_filme AS (
  SELECT
    id_filme,
    SUM(CASE WHEN genero = 1 THEN 1 ELSE 0 END) AS qtd_mulheres,
    COUNT(*) AS total_elenco,
    ROUND(SUM(CASE WHEN genero = 1 THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 4) AS perc_mulheres
  FROM elenco_genero
  GROUP BY id_filme
),
diretor_perc AS (
  SELECT
    fd.id_diretor,
    pf.id_filme,
    pf.perc_mulheres
  FROM filmes_refined_db.filmediretor fd
  JOIN perc_mulheres_por_filme pf ON fd.id_filme = pf.id_filme
)
SELECT
  CASE 
    WHEN dd.nome_diretor = 'Станислав Ростоцкий' THEN 'Stanislav Rostotsky'
    WHEN dd.nome_diretor = '片渕須直' THEN 'Sunao Katabuchi'
    ELSE dd.nome_diretor
  END AS nome_diretor,
  ROUND(AVG(diretor_perc.perc_mulheres), 4) AS media_percentual_mulheres,
  COUNT(DISTINCT diretor_perc.id_filme) AS qtd_filmes_analisados
FROM diretor_perc
JOIN filmes_refined_db.dimdiretor dd ON dd.id_diretor = diretor_perc.id_diretor
GROUP BY
  CASE 
    WHEN dd.nome_diretor = 'Станислав Ростоцкий' THEN 'Stanislav Rostotsky'
    WHEN dd.nome_diretor = '片渕須直' THEN 'Sunao Katabuchi'
    ELSE dd.nome_diretor
  END
ORDER BY media_percentual_mulheres DESC
LIMIT 10