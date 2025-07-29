CREATE OR REPLACE VIEW filmes_refined_db.vw_papeis_mulheres_por_tipo AS
SELECT
dt.decada,
CASE
WHEN fa.ordem_elenco = 0 THEN 'Principal'
WHEN fa.ordem_elenco BETWEEN 1 AND 4 THEN 'Coadjuvante'
ELSE 'Figurante'
END AS tipo_papel,
COUNT(*) AS total_personagens
FROM filmes_refined_db.filmeartista fa
JOIN filmes_refined_db.dimartista da ON fa.id_artista = da.id_artista
JOIN filmes_refined_db.fatorepresentacaofeminina frf ON frf.id_filme = fa.id_filme
JOIN filmes_refined_db.dimtempo dt ON dt.id_tempo = frf.id_tempo
WHERE da.genero = 1
GROUP BY
dt.decada,
CASE
WHEN fa.ordem_elenco = 0 THEN 'Principal'
WHEN fa.ordem_elenco BETWEEN 1 AND 4 THEN 'Coadjuvante'
ELSE 'Figurante'
END;