-- No select informei as colunas que deveriam me retornar: a de código do produto, nome do canal de vendas, nome do produto e total de quantidade vendida, na qual soma quantidade vendida para cada produto e canal.
-- Utilizei a tabela TBVENDAS e apliquei filtro com WHERE para considerar apenas vendas que foram finalizadas e usei o operador IN para especificar os canais "Ecommerce" ou "Matriz".
-- Por fim, agrupei por cdpro, nmcanalvendas, nmpro para que cada grupo representasse um produto vendido em um canal, somando as quantidades, além de ordenar os resultados em ordem crescente de quantidade vendida e limitei para mostrar os 10 primeiros produtos menos vendidos nesses canais.


SELECT 
    cdpro,
    nmcanalvendas,
    nmpro,
    SUM(qtd) AS quantidade_vendas
FROM TBVENDAS
WHERE status = 'Concluído'
  AND nmcanalvendas IN ('Ecommerce', 'Matriz')
GROUP BY cdpro, nmcanalvendas, nmpro
ORDER BY quantidade_vendas ASC
LIMIT 10