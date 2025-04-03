USE movesp;

DROP TABLE cliente;

DROP TABLE plano;

CREATE TABLE cliente(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(200) NOT NULL,
    CPF VARCHAR(14) UNIQUE NOT NULL,
    Data_nascimeto DATE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT Null,
    Senha VARCHAR(100) UNIQUE NOT NULL,
    Data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Plano(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL,
    Duracao INT NOT NULL, -- Duração do plano em dias
    Beneficios TEXT
);

DROP TABLE compras;

CREATE TABLE Compras (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    Plano_id INT NOT NULL,
    Nome_cartao VARCHAR(200) NOT NULL,
    Numero_cartao INT NOT NULL,
    Expiracao_cartao DATE NOT NULL,
    CVC INT NOT NULL,
    Data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Duracao_pl INT NOT NULL,
    Data_expiracao TIMESTAMP GENERATED ALWAYS AS (DATE_ADD(data_compra, INTERVAL Duracao_pl DAY)) STORED,
    status ENUM('ativo', 'cancelado', 'expirado') DEFAULT 'ativo',
    FOREIGN KEY (cliente_id) REFERENCES cliente(id),
    FOREIGN KEY (plano_id) REFERENCES plano(id)
);

CREATE EVENT atualizar_status_expirado
ON SCHEDULE EVERY 1 DAY
DO
    UPDATE compras
    SET status = 'expirado'
    WHERE status = 'ativo' AND Data_expiracao <= NOW();
--Funçao para  ver status dos usuarios finamicamente
CREATE VIEW compras_view AS
SELECT 
    id, cliente_id, plano_id, Data_compra, Data_expiracao,
    CASE 
        WHEN status = 'cancelado' THEN 'cancelado'
        WHEN Data_expiracao <= NOW() THEN 'expirado'
        ELSE 'ativo'
    END AS status_atual
FROM compras;

--Para chamar o VIEW
SELECT * FROM Plano;

--INSERÇÂO DE DADOS

INSERT INTO cliente (Nome, CPF, Data_nascimeto, Email, Senha) 
VALUES('Vitoria Maria', '130.496.500-79', '2006-07-25', 'vitora.maria@gmail.com', 'vm1234');

SELECT * FROM cliente;

--Vou deixar o Text em branco e depois fazer UPDATE
INSERT INTO plano (Nome, Preco, Duracao) 
VALUES('Dia', 0.50, 1);

UPDATE plano
SET Beneficios = ''
WHERE id = 1;

SELECT * FROM Plano;

INSERT INTO compras (cliente_id, plano_id, Nome_cartao, Numero_cartao, Expiracao_cartao, CVC, Duracao_pl)
VALUES (3, 2, 'Vitoria Maria', 3333, '2045-10-31', 123, (SELECT Duracao FROM plano WHERE ID = 2));

SELECT * FROM compras_view;

UPDATE compras
SET Numero_cartao = 1234567812345678
WHERE ID = 1;