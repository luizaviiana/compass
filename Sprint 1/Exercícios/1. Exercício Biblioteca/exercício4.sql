-- Iniciei o código na tabela de autores, juntei com os livros de cada autor usando  JOIN
-- Agrupei os resultados por autor e ordenei os resultados em ordem alfabética crescente pelo nome do autor

SELECT 
  autor.codautor,
  autor.nome,
  autor.nascimento,
  COUNT(livro.cod) AS quantidade
FROM 
  autor
JOIN 
  livro ON autor.codautor = livro.autor
GROUP BY 
  autor.codautor
ORDER BY 
  autor.nome ASC