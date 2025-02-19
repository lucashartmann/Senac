-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19/02/2025 às 15:03
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
-- Banco de dados: `aeroporto`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `aeroporto`
--

CREATE TABLE `aeroporto` (
  `num_avião` varchar(50) NOT NULL,
  `destino` varchar(50) NOT NULL,
  `horario_che` time NOT NULL,
  `horario_voo` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `aviao`
--

CREATE TABLE `aviao` (
  `prefixo` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `empresa` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `empregados`
--

CREATE TABLE `empregados` (
  `codigo` int(50) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `salario` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tecnico`
--

CREATE TABLE `tecnico` (
  `codigo` int(50) NOT NULL,
  `nivel` tinytext NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `aeroporto`
--
ALTER TABLE `aeroporto`
  ADD PRIMARY KEY (`num_avião`);

--
-- Índices de tabela `aviao`
--
ALTER TABLE `aviao`
  ADD PRIMARY KEY (`prefixo`);

--
-- Índices de tabela `empregados`
--
ALTER TABLE `empregados`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices de tabela `tecnico`
--
ALTER TABLE `tecnico`
  ADD PRIMARY KEY (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
