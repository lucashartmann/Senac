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
    tecnologia VARCHAR(100) NOT NULL
) ENGINE=InnoDB;