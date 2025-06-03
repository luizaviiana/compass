-- Inicialmente fiz o select* de todas as tabelas para entender os dados. No exercício ele pede
-- como retorno todas as colunas da tabela livro, então fiz o select*
-- apliquei um filtro com a data especificada de acordo com o tipo de data da coluna e ordenei

SELECT *
FROM 
  livro
WHERE 
  publicacao > '2014-12-31'
ORDER BY 
  cod ASC