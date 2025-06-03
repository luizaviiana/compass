SELECT 
  e.codeditora AS CodEditora,
  e.nome AS NometEditora,
  COUNT(l.cod) AS QuantidadeLivros
FROM 
  editora e
JOIN 
  livro l ON e.codeditora = l.editora
GROUP BY 
  e.codeditora, e.nome
ORDER BY 
  QuantidadeLivros DESC
LIMIT 5