-- Inicialmente selecionei as colunas que queria que me retornasse
--ordenei pele valor desc, para aparecer do mais caro ao mais barato
-- por meio do LIMIT 10 fiz a limitação do número que queria visualizar


SELECT 
  titulo, 
  valor
FROM 
  livro
ORDER BY 
  valor DESC
LIMIT 10
