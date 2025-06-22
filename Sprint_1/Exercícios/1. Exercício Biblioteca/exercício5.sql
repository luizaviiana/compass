-- Iniciei pela tabela de autores, juntei com a tabela de livros para saber quais livros o autor escreveu
-- Por meio do JOIN peguei a editora que publicou aquele livro e também o seu endereço
-- Realizei um filtro para editoras não situadas na região sul 
-- Por fim, ordenei o resultado por nome do autor em ordem crescente

SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON autor.codautor = livro.autor
JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY autor.nome ASC