CREATE OR REPLACE VIEW filmes_refined_db.vw_total_filmes_analisados AS
SELECT 
    COUNT(DISTINCT id_filme) AS total_filmes
FROM filmes_refined_db.fatorepresentacaofeminina