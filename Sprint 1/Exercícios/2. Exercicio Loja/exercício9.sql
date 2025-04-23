-- Iniciei o código com a subquery 'p' utilizei a TBVENDAS para conseguir filtrar por meio do WHERE apenas as vendas onde a coluna status fosse igual a Concluído e o BETWEEN para informar que também deveriam estar em um intervalo de data definido, agrupei pelo nome e código do produto. 
-- No select da subquery informei a coluna 'cdpro', 'nmpro' e fiz a soma de valores da coluna qtd para saber o produto que teve mais vendas de alias 'total_vendido'.
-- Para finalizar a subquery ordenei pelo total_vendido do maior para menor e limitei a visualização para que retornasse apenas 1
-- Finalizei com o SELECT para que retornasse o valor do código do produto mais vendido e o nome do produto mais vendido

SELECT 
    p.cdpro, 
    p.nmpro
FROM (
    SELECT 
        cdpro, 
        nmpro, 
        SUM(qtd) AS total_vendido
    FROM TBVENDAS
    WHERE status = 'Concluído'
      AND dtven BETWEEN '2014-02-03' AND '2018-02-02'
    GROUP BY cdpro, nmpro
    ORDER BY total_vendido DESC
    LIMIT 1
) AS p