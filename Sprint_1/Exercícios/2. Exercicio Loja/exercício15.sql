-- No SELECT informei a coluna que deveria retornar: código da venda.
-- Realizei a consulta na TBVENDAS e apliquei um filtro com WHERE para filtrar apenas as vendas que foram deletadas, a coluna deletado armazena o valor 1 quando a venda é deletada e 0 quando não foi deletada, assim,  vamos pegar as vendas com deletado = 1.
-- Por fim, ordenei para exibir o resultado em ordem crescente do código da venda


SELECT cdven
FROM TBVENDAS
WHERE deletado = 1
ORDER BY cdven ASC