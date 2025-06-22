-- No SELECT informei as colunas que deveriam retornar: estado, nome do produto e quantidade_media, onde realizei o cálculo da média da quantidade vendida e arredondada para 4 casas decimais.
-- Utilizei a TBVENDAS e filtrei por meio do WHERE apenas as vendas com status concluído, agrupei os dados por estado e nome do produto e ordenei o resultado primeiro por estado e depois por nome do produto.

SELECT 
    estado,
    nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM TBVENDAS
WHERE status = 'Concluído'
GROUP BY estado, nmpro
ORDER BY estado, nmpro