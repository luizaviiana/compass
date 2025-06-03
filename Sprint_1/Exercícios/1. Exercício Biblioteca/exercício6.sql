-- Por meio do SELECT informei as colunas que deveriam retornar, a coluna quantidade_publicacoes fiz um COUNT para contagem de livros cadastrados do autor.
-- Realizei o Join da tabela de autor com a de livros, agrupei os dados pelo autor, ordenei do autor com mais livro para o de menos e limitei a visualização para 1 autor


SELECT 
  autor.codautor,
  autor.nome,
  COUNT(livro.cod) AS quantidade_publicacoes
FROM 
  autor
JOIN 
  livro ON autor.codautor = livro.autor
GROUP BY 
  autor.codautor
ORDER BY 
  quantidade_publicacoes DESC
LIMIT 1