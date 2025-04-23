-- View: Dimensão Tempo
CREATE VIEW dim_tempo AS
SELECT DISTINCT
    data_locacao AS data_tempo,
    CAST(strftime('%d', data_locacao) AS INTEGER) AS dia,
    CAST(strftime('%m', data_locacao) AS INTEGER) AS mes,
    CAST(strftime('%Y', data_locacao) AS INTEGER) AS ano
FROM tbl_locacoes;

-- View: Dimensão Cliente
CREATE VIEW dim_cliente AS
SELECT 
    id_cliente,
    nome_cliente,
    cidade_cliente,
    estado_cliente,
    pais_cliente
FROM tbl_clientes;

-- View: Dimensão Carro
CREATE VIEW dim_carro AS
SELECT 
    c.id_carro,
    c.km_rodado,
    c.chassi,
    c.marca,
    c.modelo,
    c.ano,
    f.tipo_combustivel
FROM tbl_carros c
JOIN tbl_combustiveis f ON c.id_combustivel = f.id_combustivel;

-- View: Dimensão Vendedor
CREATE VIEW dim_vendedor AS
SELECT 
    id_vendedor,
    nome_vendedor,
    sexo,
    estado
FROM tbl_vendedores;

-- View: Fato Locação
CREATE VIEW fato_locacao AS
SELECT 
    id_locacao,
    id_cliente,
    id_carro,
    id_vendedor,
    data_locacao AS data_tempo,
    qtd_diarias,
    valor_diaria,
    qtd_diarias * valor_diaria AS total_locacao
FROM tbl_locacoes;