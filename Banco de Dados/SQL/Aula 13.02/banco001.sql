-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 13/02/2025 às 15:14
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
-- Banco de dados: `banco001`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `tabela001`
--

CREATE TABLE `tabela001` (
  `id_tabela001` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `sobrenome` varchar(30) NOT NULL,
  `idade` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tabela002`
--

CREATE TABLE `tabela002` (
  `id_tabela002` int(11) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `idade` int(3) NOT NULL,
  `endereco` varchar(50) NOT NULL,
  `numero_residencia` int(4) NOT NULL,
  `complemento` varchar(10) DEFAULT NULL,
  `bairro` varchar(50) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `uf` char(2) NOT NULL,
  `data_nascimento` date NOT NULL,
  `sexo` char(1) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `obs` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `tabela003`
--

CREATE TABLE `tabela003` (
  `id_tabela003` int(11) NOT NULL,
  `nome_produto` varchar(50) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `peso` float(5,2) NOT NULL,
  `preco` double(5,2) NOT NULL,
  `data_entrada` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `tabela001`
--
ALTER TABLE `tabela001`
  ADD PRIMARY KEY (`id_tabela001`);

--
-- Índices de tabela `tabela002`
--
ALTER TABLE `tabela002`
  ADD PRIMARY KEY (`id_tabela002`);

--
-- Índices de tabela `tabela003`
--
ALTER TABLE `tabela003`
  ADD PRIMARY KEY (`id_tabela003`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tabela001`
--
ALTER TABLE `tabela001`
  MODIFY `id_tabela001` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tabela002`
--
ALTER TABLE `tabela002`
  MODIFY `id_tabela002` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tabela003`
--
ALTER TABLE `tabela003`
  MODIFY `id_tabela003` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
