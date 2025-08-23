-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19/03/2025 às 14:38
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `escola`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `aluno`
--

CREATE TABLE `aluno` (
  `num_matri` int(11) NOT NULL,
  `data_nasci` date NOT NULL,
  `rua` varchar(100) DEFAULT NULL,
  `bairro` varchar(50) DEFAULT NULL,
  `cep` varchar(10) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `genero` char(1) DEFAULT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `aluno`
--

INSERT INTO `aluno` (`num_matri`, `data_nasci`, `rua`, `bairro`, `cep`, `cidade`, `genero`, `nome`) VALUES
(10001, '2000-06-15', 'Rua dos Estudantes, 100', 'Centro', '01234-567', 'São Paulo', 'M', 'Rafael Mendes'),
(10002, '2001-04-22', 'Av. das Universidades, 200', 'Pinheiros', '02345-678', 'São Paulo', 'F', 'Juliana Costa'),
(10003, '1999-11-10', 'Rua Doutor Silva, 300', 'Saúde', '03456-789', 'São Paulo', 'M', 'Bruno Almeida'),
(10004, '2002-02-28', 'Av. Paulista, 400', 'Bela Vista', '04567-890', 'São Paulo', 'F', 'Carolina Souza'),
(10005, '2000-09-17', 'Rua da Tecnologia, 500', 'Vila Mariana', '05678-901', 'São Paulo', 'M', 'Daniel Ferreira');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cursos`
--

CREATE TABLE `cursos` (
  `id_cursos` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `turno` varchar(20) NOT NULL,
  `area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cursos`
--

INSERT INTO `cursos` (`id_cursos`, `nome`, `turno`, `area`) VALUES
(1, 'Engenharia de Software', 'Manhã', 'Tecnologia'),
(2, 'Administração', 'Noite', 'Negócios'),
(3, 'Medicina', 'Integral', 'Saúde'),
(4, 'Direito', 'Noite', 'Humanas'),
(5, 'Ciência da Computação', 'Tarde', 'Tecnologia');

-- --------------------------------------------------------

--
-- Estrutura para tabela `dependentes`
--

CREATE TABLE `dependentes` (
  `nome` varchar(100) NOT NULL,
  `grau_parentesco` varchar(50) DEFAULT NULL,
  `cod_depe` int(11) NOT NULL,
  `data_nasc` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `dependentes`
--

INSERT INTO `dependentes` (`nome`, `grau_parentesco`, `cod_depe`, `data_nasc`) VALUES
('Miguel Silva', 'Filho', 501, '2015-03-12'),
('Beatriz Oliveira', 'Filha', 502, '2017-07-25'),
('Lucas Santos', 'Filho', 503, '2010-11-30'),
('Sophia Pereira', 'Filha', 504, '2016-05-18'),
('Pedro Lima', 'Filho', 505, '2014-09-22');

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplina`
--

CREATE TABLE `disciplina` (
  `cod_disc` int(11) NOT NULL,
  `descricao` varchar(200) NOT NULL,
  `codigo_sala` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `disciplina`
--

INSERT INTO `disciplina` (`cod_disc`, `descricao`, `codigo_sala`) VALUES
(2001, 'Programação Orientada a Objetos', 101),
(2002, 'Gestão Empresarial', 102),
(2003, 'Anatomia Humana', 103),
(2004, 'Direito Constitucional', 104),
(2005, 'Estrutura de Dados', 105);

-- --------------------------------------------------------

--
-- Estrutura para tabela `docente`
--

CREATE TABLE `docente` (
  `cod_doce` int(11) NOT NULL,
  `endereco` varchar(200) NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `codigo_dependente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `docente`
--

INSERT INTO `docente` (`cod_doce`, `endereco`, `telefone`, `nome`, `codigo_dependente`) VALUES
(1001, 'Rua das Flores, 123 - Centro', 0, 'Ana Silva', 501),
(1002, 'Av. Principal, 456 - Jardins', 0, 'Carlos Oliveira', 501),
(1003, 'Rua do Comércio, 789 - Vila Nova', 0, 'Maria Santos', 501),
(1004, 'Av. Brasil, 321 - Centro', 0, 'João Pereira', 501),
(1005, 'Rua das Palmeiras, 654 - Parque Verde', 0, 'Fernanda Lima', 501);

-- --------------------------------------------------------

--
-- Estrutura para tabela `matricula`
--

CREATE TABLE `matricula` (
  `id` int(11) NOT NULL,
  `data_matri` date NOT NULL,
  `numero_matricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `matricula`
--

INSERT INTO `matricula` (`id`, `data_matri`, `numero_matricula`) VALUES
(1, '2022-02-10', 10001),
(2, '2022-02-11', 10002),
(3, '2022-02-09', 10003),
(4, '2022-02-12', 10004),
(5, '2022-02-08', 10005);

-- --------------------------------------------------------

--
-- Estrutura para tabela `sala`
--

CREATE TABLE `sala` (
  `cod_sala` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `localizacao` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `sala`
--

INSERT INTO `sala` (`cod_sala`, `nome`, `localizacao`) VALUES
(101, 'Laboratório de Informática', 'Bloco A - Térreo'),
(102, 'Sala de Aula 1', 'Bloco B - 1º Andar'),
(103, 'Auditório', 'Bloco C - Térreo'),
(104, 'Laboratório de Anatomia', 'Bloco D - 2º Andar'),
(105, 'Sala de Estudos', 'Biblioteca - 3º Andar');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `aluno`
--
ALTER TABLE `aluno`
  ADD PRIMARY KEY (`num_matri`);

--
-- Índices de tabela `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_cursos`);

--
-- Índices de tabela `dependentes`
--
ALTER TABLE `dependentes`
  ADD PRIMARY KEY (`cod_depe`);

--
-- Índices de tabela `disciplina`
--
ALTER TABLE `disciplina`
  ADD PRIMARY KEY (`cod_disc`),
  ADD KEY `codigo_sala` (`codigo_sala`);

--
-- Índices de tabela `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`cod_doce`),
  ADD KEY `codigo_dependente` (`codigo_dependente`);

--
-- Índices de tabela `matricula`
--
ALTER TABLE `matricula`
  ADD PRIMARY KEY (`id`),
  ADD KEY `numero_matricula` (`numero_matricula`);

--
-- Índices de tabela `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`cod_sala`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `matricula`
--
ALTER TABLE `matricula`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `disciplina`
--
ALTER TABLE `disciplina`
  ADD CONSTRAINT `disciplina_ibfk_1` FOREIGN KEY (`codigo_sala`) REFERENCES `sala` (`cod_sala`);

--
-- Restrições para tabelas `docente`
--
ALTER TABLE `docente`
  ADD CONSTRAINT `docente_ibfk_1` FOREIGN KEY (`codigo_dependente`) REFERENCES `dependentes` (`cod_depe`);

--
-- Restrições para tabelas `matricula`
--
ALTER TABLE `matricula`
  ADD CONSTRAINT `matricula_ibfk_1` FOREIGN KEY (`numero_matricula`) REFERENCES `aluno` (`num_matri`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
