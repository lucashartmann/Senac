-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 21/02/2025 às 15:41
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
-- Banco de dados: `tcheuber`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `mecanico`
--

CREATE TABLE `mecanico` (
  `nome` varchar(30) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(2) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `celular` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `mecanico`
--

INSERT INTO `mecanico` (`nome`, `endereco`, `cidade`, `estado`, `cpf`, `celular`) VALUES
('Jorge', 'Bento Gonçalves', 'Porto Alegre', 'RS', '0235314564', 5193435635),
('Giovani', 'João Pessoa 279', 'Bento Gonçalves', 'RS', '05634564587', 519485893959);

-- --------------------------------------------------------

--
-- Estrutura para tabela `motorista`
--

CREATE TABLE `motorista` (
  `nome_completo` varchar(100) NOT NULL,
  `categoria` char(1) NOT NULL,
  `numero` int(11) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(2) NOT NULL,
  `celular` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `motorista`
--

INSERT INTO `motorista` (`nome_completo`, `categoria`, `numero`, `cpf`, `endereco`, `cidade`, `estado`, `celular`) VALUES
('Marcelo Fernando de Jesus', 'A', 233, '02002030405', 'Avenida Bentinho da Silva', 'Araraquara', 'SP', 51000909876);

-- --------------------------------------------------------

--
-- Estrutura para tabela `servico`
--

CREATE TABLE `servico` (
  `numero` int(11) NOT NULL,
  `data_solicitacao` date NOT NULL,
  `data_problema` date NOT NULL,
  `nome_veiculo` varchar(30) NOT NULL,
  `nome_motorista` varchar(30) NOT NULL,
  `placa` varchar(7) NOT NULL,
  `servico` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `servico`
--

INSERT INTO `servico` (`numero`, `data_solicitacao`, `data_problema`, `nome_veiculo`, `nome_motorista`, `placa`, `servico`) VALUES
(2, '2025-02-24', '2025-02-20', 'Perua do seu João', 'Luis', 'RGS200', 'Foi feito calibragem de pneus e conserto do motor'),
(232, '2021-04-02', '2020-12-30', 'Lambretinha do seu zé', 'Alceu', 'SSI-122', 'Foi enchido o pneu');

-- --------------------------------------------------------

--
-- Estrutura para tabela `veiculo`
--

CREATE TABLE `veiculo` (
  `nome` varchar(30) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `modelo` varchar(20) NOT NULL,
  `placa` varchar(7) NOT NULL,
  `ano` int(4) NOT NULL,
  `numero_chassi` int(6) NOT NULL,
  `cor` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `veiculo`
--

INSERT INTO `veiculo` (`nome`, `marca`, `modelo`, `placa`, `ano`, `numero_chassi`, `cor`) VALUES
('Bicicleta', 'BMX', 'PRO X', 'AAS-233', 2003, 224, 'Vermelha');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `mecanico`
--
ALTER TABLE `mecanico`
  ADD PRIMARY KEY (`cpf`);

--
-- Índices de tabela `motorista`
--
ALTER TABLE `motorista`
  ADD PRIMARY KEY (`numero`),
  ADD UNIQUE KEY `cpf` (`cpf`);

--
-- Índices de tabela `servico`
--
ALTER TABLE `servico`
  ADD PRIMARY KEY (`numero`);

--
-- Índices de tabela `veiculo`
--
ALTER TABLE `veiculo`
  ADD PRIMARY KEY (`placa`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `motorista`
--
ALTER TABLE `motorista`
  MODIFY `numero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=234;

--
-- AUTO_INCREMENT de tabela `servico`
--
ALTER TABLE `servico`
  MODIFY `numero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=233;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
