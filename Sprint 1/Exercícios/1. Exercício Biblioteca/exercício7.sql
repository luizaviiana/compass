-- No SELECT informei apenas a coluna que queria que retornasse
-- Comecei pela tabela autor, pois irá juntar os autores com seus livros e, mesmo se algum autor não tiver livro, ainda aparecerá na com contagem por causa do LEFT JOIN
-- Utilizei o filtro WHERE para aparecer apenas  os autores que não têm nenhum livro
-- Após isso ordenei pelo nome

SELECT autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor
WHERE livro.cod IS NULL
ORDER BY autor.nome ASC