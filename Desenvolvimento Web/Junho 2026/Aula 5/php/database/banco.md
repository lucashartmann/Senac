-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS techtalent_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE techtalent_db;

-- Criar a tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    idUsuario INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL, -- Tamanho 255 para suportar Hashes de senha no futuro
    perfil ENUM('admin', 'user') NOT NULL DEFAULT 'user',
    nome_exibicao VARCHAR(100)
) ENGINE=InnoDB;

-- Inserir dados de teste
-- Nota: Em um sistema real, a senha nunca seria '123'. 
-- Usaríamos password_hash('123', PASSWORD_DEFAULT)
INSERT INTO usuarios (login, senha, perfil, nome_exibicao) VALUES 
('claudio.admin', '123', 'admin', 'Claudio Roberto (Gestor)'),
('aluno.tech', 'abc', 'user', 'Estudante Tech');


- Tabela de Talentos 
CREATE TABLE IF NOT EXISTS talentos (
    idTalento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fone VARCHAR(20) NOT NULL,
    tecnologia VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    curriculo varchar(255) NULL;
) ENGINE=InnoDB;

INSERT INTO talentos (nome, email, fone, tecnologia, senha) VALUES
('Ana Silva', 'ana@email.com', '11999991111', 'PHP', '123'),
('Bruno Lima', 'bruno@email.com', '11999992222', 'Java', '321'),
('Carlos Souza', 'carlos@email.com', '11999993333', 'Python', '123'),
('Daniela Reis', 'daniela@email.com', '11999994444', 'JavaScript', '456'),
('Lucas', 'lucas@email.com', '00000000000', 'C#, Java', '789'),
('Eduardo Costa', 'eduardo@email.com', '11999995555', 'C#', '789');
