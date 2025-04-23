-- Iniciei o código com a subquery 'v', utilizei a TBVENDAS para conseguir filtrar por meio do WHERE apenas as vendas onde a coluna status fosse igual a Concluído, agrupei pelo código do vendedor, fiz a contagem de linhas (vendas de cada vendedor) por meio do COUNT, ordenei os vendedores pelo total_vendas do maior para o menor e limitei a 1 para que retornasse o que mais vendeu
-- Por meio do JOIN fiz a junção das duas tabelas: TBVENDEDOR de alias 'vdd' com a subquery 'v' para conseguirmos o nome do vendedor que mais vendeu
-- No select pedi que me retornasse o nome do vendedor e o código

SELECT 
    v.cdvdd, 
    vdd.nmvdd
FROM (
    SELECT 
        cdvdd, 
        COUNT(*) AS total_vendas
    FROM TBVENDAS
    WHERE status = 'Concluído'
    GROUP BY cdvdd
    ORDER BY total_vendas DESC
    LIMIT 1
) AS v
JOIN TBVENDEDOR vdd ON v.cdvdd = vdd.cdvdd