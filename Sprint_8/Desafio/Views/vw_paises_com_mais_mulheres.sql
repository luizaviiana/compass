CREATE OR REPLACE VIEW filmes_refined_db.vw_paises_com_mais_mulheres AS
WITH elenco_genero AS (
  SELECT
    fa.id_filme,
    da.genero
  FROM filmes_refined_db.filmeartista fa
  JOIN filmes_refined_db.dimartista da ON fa.id_artista = da.id_artista
),
stats AS (
  SELECT
    frf.id_pais,
    COUNT(*) AS total_personagens,
    SUM(CASE WHEN eg.genero = 1 THEN 1 ELSE 0 END) AS total_mulheres
  FROM filmes_refined_db.fatorepresentacaofeminina frf
  JOIN elenco_genero eg ON frf.id_filme = eg.id_filme
  GROUP BY frf.id_pais
)
SELECT
  dp.nome_pais,
  ROUND(CAST(s.total_mulheres AS DOUBLE) / s.total_personagens, 4) AS percentual_mulheres
FROM stats s
JOIN filmes_refined_db.dimpais dp ON dp.id_pais = s.id_pais
ORDER BY percentual_mulheres DESC