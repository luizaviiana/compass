SELECT 
  l.cod AS CodLivro,
  l.titulo AS Titulo,
  a.codautor AS CodAutor,
  a.nome AS NomeAutor,
  l.valor AS Valor,
  e.codeditora AS CodEditora,
  e.nome AS NomeEditora
FROM 
  livro l
LEFT JOIN autor a ON l.autor = a.codautor
LEFT JOIN editora e  ON l.editora = e.codeditora
ORDER BY l.valor DESC
LIMIT 10