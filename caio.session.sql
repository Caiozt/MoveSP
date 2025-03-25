DROP TABLE cliente;

CREATE TABLE cliente(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(200) NOT NULL,
    CPF INT UNIQUE NOT NULL,
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

CREATE TABLE Compras (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Usuario_id INT NOT NULL,
    Plano_id INT NOT NULL,
    Data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Data_expiracao TIMESTAMP GENERATED ALWAYS AS (DATE_ADD(data_compra, INTERVAL duracao DAY)) STORED,
    status ENUM('ativo', 'cancelado', 'expirado') DEFAULT 'ativo',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (plano_id) REFERENCES planos(id)
);

CREATE EVENT atualizar_status_expirado
ON SCHEDULE EVERY 1 DAY
DO
    UPDATE compras
    SET status = 'expirado'
    WHERE status = 'ativo' AND data_expiracao <= NOW();

CREATE VIEW compras_view AS
SELECT 
    id, usuario_id, plano_id, data_compra, data_expiracao,
    CASE 
        WHEN status = 'cancelado' THEN 'cancelado'
        WHEN data_expiracao <= NOW() THEN 'expirado'
        ELSE 'ativo'
    END AS status_atual
FROM compras;