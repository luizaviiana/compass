-- Tabela de Clientes
CREATE TABLE tbl_clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    cidade_cliente VARCHAR(100),
    estado_cliente VARCHAR(50),
    pais_cliente VARCHAR(50)
);

-- Tabela de Combustíveis
CREATE TABLE tbl_combustiveis (
    id_combustivel INTEGER PRIMARY KEY,
    tipo_combustivel VARCHAR(20)
);

-- Tabela de Carros
CREATE TABLE tbl_carros (
    id_carro INTEGER PRIMARY KEY,
    km_rodado INTEGER,
    chassi VARCHAR(20),
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano INTEGER,
    id_combustivel INTEGER,
    FOREIGN KEY (id_combustivel) REFERENCES tbl_combustiveis(id_combustivel)
);

-- ‍Tabela de Vendedores
CREATE TABLE tbl_vendedores (
    id_vendedor INTEGER PRIMARY KEY,
    nome_vendedor VARCHAR(100),
    sexo SMALLINT,
    estado VARCHAR(50)
);

-- Tabela de Locações
CREATE TABLE tbl_locacoes (
    id_locacao INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    id_carro INTEGER,
    id_vendedor INTEGER,
    data_locacao DATE,
    hora_locacao TIME,
    qtd_diarias INTEGER,
    valor_diaria DECIMAL(10,2),
    data_entrega DATE,
    hora_entrega TIME,
    FOREIGN KEY (id_cliente) REFERENCES tbl_clientes(id_cliente),
    FOREIGN KEY (id_carro) REFERENCES tbl_carros(id_carro),
    FOREIGN KEY (id_vendedor) REFERENCES tbl_vendedores(id_vendedor)
);