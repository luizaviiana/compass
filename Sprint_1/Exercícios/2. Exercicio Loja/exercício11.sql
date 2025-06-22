-- Iniciei o código no FROM com a tabela TBVENDAS e aplicando o filtro com WHERE para considerar somente as vendas concluídas.
-- No SELECT informei as colunas que deveriam retornar: o código do cliente, nome do cliente e o gasto, para essa última coluna realizei o cálculo multiplicando a quantidade de produtos e o valor unitário, somei os valores de todas as compras feitas e arredondei o valor final para 2 casas decimais.
-- Por fim, voltando ao código agrupei por código e nome para que a soma funcione por cliente e agrupei para que o resultado fosse do maior gasto para o menor

SELECT 
    cdcli,
    nmcli,
    ROUND(SUM(qtd * vrunt), 2) AS gasto
FROM TBVENDAS
WHERE status = 'Concluído'
GROUP BY cdcli, nmcli
ORDER BY gasto DESC
LIMIT 1