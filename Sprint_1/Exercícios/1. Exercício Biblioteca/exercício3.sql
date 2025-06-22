-- Utilizei o COUNT para fazer a coluna de contagem de livros que cada editora publicou
-- Após isso também coloquei as colunas que queria que retornassem
-- Por meio do join pude juntar a editora com os livros e com os endereços
-- Agrupei os livros por editora para contagem, ordenei da editora que publicou mais livros para a que publicou menos e limitei para 5 a visualização de editoras

SELECT 
  COUNT(livro.cod) AS quantidade,
  editora.nome,
  endereco.estado,
  endereco.cidade
FROM 
  livro
JOIN 
  editora ON livro.editora = editora.codeditora
JOIN 
  endereco ON editora.endereco = endereco.codendereco
GROUP BY 
  editora.codeditora
ORDER BY 
  quantidade DESC
LIMIT 5