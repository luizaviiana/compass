SELECT 
  l.cod AS CodLivro,
  l.titulo AS Titulo,
  l.autor AS CodAutor,
  l.valor AS Valor,
  l.editora AS CodEditora,
  e.nome AS NomeEditora
FROM 
  livro l
LEFT JOIN 
  editora e ON l.editora = e.codeditora
ORDER BY 
  l.valor DESC
LIMIT 10