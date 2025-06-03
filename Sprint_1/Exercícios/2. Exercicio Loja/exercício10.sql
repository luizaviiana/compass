-- Primeiro levantei os dados pedidos no enunciado que seria de calcular a comissão dos vendedores, analisando o total vendido por cada um, a porcentagem da comissão e considerar apenas as vendas que estivessem status de concluída.
-- Iniciei o código com o from da tabela TBVENDAS de alias 'v'fiz um JOIN com a tabela TBVENDEDOR de alias 'vdd', usei o código de vendedor como chave para conseguir acessar os dados das vendas e dos vendedores, apliquei um filtro com WHERE para considerar apenas as vendas com status de Concluído
-- No SELECT informei as colunas que deveriam ser apresentadas, a primeira foi o do nome do vendedor, a segunda foi o valor total de vendas e para calcular multipliquei a quantidade de produtos vendidos pelo valor unitário, somei todas as vendas e arredondei o valor final para 2 casas decimais, a terceira coluna fiz o cálculo da comissão, assim, utilizei o total de vendas e multipliquei pelo resultado da perccomissao dividida por 100, já que o valor estava em porcentagem, por fim arredondei a comissão final para 2 casas decimais
-- Por fim, agrupei os resultados por vendedor e comissao, além de ordenar do vendedor que ganhou mais comissão para o de menor

SELECT 
    vdd.nmvdd AS vendedor,
    ROUND(SUM(v.qtd * v.vrunt), 2) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * (vdd.perccomissao / 100.0), 2) AS comissao
FROM TBVENDAS v
JOIN TBVENDEDOR vdd ON v.cdvdd = vdd.cdvdd
WHERE v.status = 'Concluído'
GROUP BY vdd.nmvdd, vdd.perccomissao
ORDER BY comissao DESC