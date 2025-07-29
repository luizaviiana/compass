CREATE OR REPLACE VIEW "vw_tendencias_representacao" AS 
WITH
  elenco_completo AS (
   SELECT
     fa.id_filme
   , da.genero
   FROM
     (filmes_refined_db.filmeartista fa
   INNER JOIN filmes_refined_db.dimartista da ON (fa.id_artista = da.id_artista))
) 
, stats AS (
   SELECT
     id_filme
   , COUNT(*) total_elenco
   , SUM((CASE WHEN (genero = 1) THEN 1 ELSE 0 END)) mulheres
   , SUM((CASE WHEN (genero = 2) THEN 1 ELSE 0 END)) homens
   FROM
     elenco_completo
   GROUP BY id_filme
) 
SELECT
  f.id_filme
, f.titulo_principal
, f.nota_media
, f.popularidade
, s.total_elenco
, s.mulheres
, s.homens
, ((s.total_elenco - s.mulheres) - s.homens) desconhecido
, ROUND(((s.mulheres * 1E2) / s.total_elenco), 2) percentual_mulheres
, ROUND(((s.homens * 1E2) / s.total_elenco), 2) percentual_homens
, ROUND(((((s.total_elenco - s.mulheres) - s.homens) * 1E2) / s.total_elenco), 2) percentual_desconhecido
, (CASE WHEN (((s.mulheres * 1E2) / s.total_elenco) <= 20) THEN 'Baixa representatividade' WHEN (((s.mulheres * 1E2) / s.total_elenco) <= 50) THEN 'Representatividade moderada' WHEN (((s.mulheres * 1E2) / s.total_elenco) <= 80) THEN 'Representatividade significativa' ELSE 'Alta representatividade' END) faixa_representatividade
FROM
  (stats s
INNER JOIN filmes_refined_db.fatorepresentacaofeminina f ON (f.id_filme = s.id_filme))
WHERE (s.total_elenco > 0)