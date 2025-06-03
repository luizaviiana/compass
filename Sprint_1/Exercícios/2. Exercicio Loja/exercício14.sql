-- No SELECT informei as colunas que deveriam me retornar os resultados: a do nome do estado e o de gastomedio, na qual realizei o cálculo do  valor bruto de cada venda (qtd * vrunt) e a média desse valor arredondando para 2 casas decimais.
-- Por meio da TBVENDAS realizei o filtro  dos registros para considerar apenas as vendas que foram concluídas, agrupei os dados por estado, para saber o gasto médio por estado e ordenei  o resultado de forma decrescente para mostrar primeiro os estados com maior gasto médio.

SELECT 
    estado,
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio
FROM TBVENDAS
WHERE status = 'Concluído'
GROUP BY estado
ORDER BY gastomedio DESC