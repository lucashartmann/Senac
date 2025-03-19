-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19/03/2025 às 16:03
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
-- Banco de dados: `escola01`
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `aluno`
--

INSERT INTO `aluno` (`num_matri`, `data_nasci`, `rua`, `bairro`, `cep`, `cidade`, `genero`, `nome`) VALUES
(10006, '2001-02-15', 'Rua dos Estudantes, 101', 'Centro', '01234-568', 'São Paulo', 'M', 'Lucas Silva'),
(10007, '2001-05-22', 'Av. das Universidades, 201', 'Pinheiros', '02345-679', 'São Paulo', 'F', 'Camila Oliveira'),
(10008, '1998-10-10', 'Rua Doutor Silva, 301', 'Saúde', '03456-790', 'São Paulo', 'M', 'Felipe Almeida'),
(10009, '2003-03-28', 'Av. Paulista, 401', 'Bela Vista', '04567-891', 'São Paulo', 'F', 'Laura Souza'),
(10010, '2001-10-17', 'Rua da Tecnologia, 501', 'Vila Mariana', '05678-902', 'São Paulo', 'M', 'Tiago Ferreira');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cursos`
--

CREATE TABLE `cursos` (
  `id_cursos` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `turno` varchar(20) NOT NULL,
  `area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `cursos`
--

INSERT INTO `cursos` (`id_cursos`, `nome`, `turno`, `area`) VALUES
(1, 'Engenharia de Computação', 'Manhã', 'Tecnologia'),
(2, 'Gestão Empresarial', 'Noite', 'Negócios'),
(3, 'Medicina Veterinária', 'Integral', 'Saúde'),
(4, 'Direito Penal', 'Noite', 'Humanas'),
(5, 'Sistemas de Informação', 'Tarde', 'Tecnologia');

-- --------------------------------------------------------

--
-- Estrutura para tabela `dependentes`
--

CREATE TABLE `dependentes` (
  `nome` varchar(100) NOT NULL,
  `grau_parentesco` varchar(50) DEFAULT NULL,
  `cod_depe` int(11) NOT NULL,
  `data_nasc` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `dependentes`
--

INSERT INTO `dependentes` (`nome`, `grau_parentesco`, `cod_depe`, `data_nasc`) VALUES
('Ana Silva', 'Filha', 501, '2016-03-12'),
('Carlos Oliveira', 'Filho', 502, '2018-07-25'),
('Beatriz Santos', 'Filha', 503, '2011-11-30'),
('Lucas Pereira', 'Filho', 504, '2017-05-18'),
('Renato Lima', 'Filho', 505, '2015-09-22');

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplina`
--

CREATE TABLE `disciplina` (
  `cod_disc` int(11) NOT NULL,
  `descricao` varchar(200) NOT NULL,
  `codigo_sala` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `docente`
--

INSERT INTO `docente` (`cod_doce`, `endereco`, `telefone`, `nome`, `codigo_dependente`) VALUES
(1001, 'Rua das Flores, 123', 1122334455, 'Ana Silva', 501),
(1002, 'Av. Principal, 456', 2233445566, 'Carlos Oliveira', 502),
(1003, 'Rua do Comércio, 789', 3344556677, 'Maria Santos', 503),
(1004, 'Av. Brasil, 321', 4455667788, 'João Pereira', 504),
(1005, 'Rua das Palmeiras, 654', 5566778899, 'Fernanda Lima', 505);

-- --------------------------------------------------------

--
-- Estrutura para tabela `matricula`
--

CREATE TABLE `matricula` (
  `id` int(11) NOT NULL,
  `data_matri` date NOT NULL,
  `numero_matricula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `matricula`
--

INSERT INTO `matricula` (`id`, `data_matri`, `numero_matricula`) VALUES
(1, '2022-03-10', 10006),
(2, '2022-03-11', 10007),
(3, '2022-03-09', 10008),
(4, '2022-03-12', 10009),
(5, '2022-03-08', 10010);

-- --------------------------------------------------------

--
-- Estrutura para tabela `sala`
--

CREATE TABLE `sala` (
  `cod_sala` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `localizacao` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `sala`
--

INSERT INTO `sala` (`cod_sala`, `nome`, `localizacao`) VALUES
(101, 'Laboratório de Engenharia de Software', 'Bloco A - Térreo'),
(102, 'Sala de Aula 2', 'Bloco B - 1º Andar'),
(103, 'Auditório Principal', 'Bloco C - Térreo'),
(104, 'Laboratório de Ciências', 'Bloco D - 2º Andar'),
(105, 'Sala de Estudos Avançados', 'Biblioteca - 3º Andar');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
