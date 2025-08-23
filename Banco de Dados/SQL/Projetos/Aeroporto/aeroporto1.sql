-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 27/03/2025 às 15:13
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
-- Banco de dados: `aeroporto1`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `aeroporto`
--

CREATE TABLE `aeroporto` (
  `id_aeroporto` int(11) NOT NULL,
  `capacidade` int(200) NOT NULL,
  `peso_max` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `aeroporto`
--

INSERT INTO `aeroporto` (`id_aeroporto`, `capacidade`, `peso_max`) VALUES
(1, 200, 1000),
(2, 100, 1000),
(3, 50, 1000.1),
(4, 20, 2000),
(5, 10, 30000);

-- --------------------------------------------------------

--
-- Estrutura para tabela `aviao`
--

CREATE TABLE `aviao` (
  `id_aviao` int(11) NOT NULL,
  `prefixo` varchar(10) NOT NULL,
  `cod_modelo` int(11) NOT NULL,
  `cod_empresa` int(11) NOT NULL,
  `obs` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `aviao`
--

INSERT INTO `aviao` (`id_aviao`, `prefixo`, `cod_modelo`, `cod_empresa`, `obs`) VALUES
(1, 'ADSDS22', 1, 1, NULL),
(2, 'FSFSF21', 2, 1, NULL),
(3, 'FSFS1', 3, 2, NULL),
(4, 'FSDGFD', 4, 4, NULL),
(5, 'ASASEW3', 5, 3, NULL);

-- --------------------------------------------------------

--
-- Estrutura para tabela `cidade`
--

CREATE TABLE `cidade` (
  `id_cidade` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `cidade`
--

INSERT INTO `cidade` (`id_cidade`, `nome`) VALUES
(1, 'Porto Alegre'),
(2, 'Buenos Aires'),
(3, 'Caxias'),
(4, 'Natal'),
(5, 'Lisboa');

-- --------------------------------------------------------

--
-- Estrutura para tabela `empregados`
--

CREATE TABLE `empregados` (
  `id_empregados` int(11) NOT NULL,
  `codigo` int(11) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `cod_cidade` int(11) NOT NULL,
  `cod_estado` int(11) NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `empregados`
--

INSERT INTO `empregados` (`id_empregados`, `codigo`, `nome_completo`, `endereco`, `cod_cidade`, `cod_estado`, `telefone`, `email`) VALUES
(1, 1, 'Jorge Ferreira Abreu', 'Av. Santo Agostinho 29', 1, 1, 51111111111, 'Jorge@hotmail.com'),
(2, 2, 'Marcielly Pereira Borges', 'Lima e Silva 400', 1, 1, 51222222222, 'Maumau@hotmail.com'),
(3, 3, 'Rosane Fernanda dos Santos', 'Av. Bento Gonçalves 204', 2, 2, 51333333333, 'Rosane@gmail.com'),
(4, 4, 'Lisangêla Thais Silva', 'Travessa Ferreira 409', 3, 3, 51444444444, 'Lisangêla@hotmail.com'),
(5, 5, 'Thais Augusta Fernandes', 'Zélia Maria A. Bichequer 10', 4, 5, 51555555555, 'Thais@hotmail.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `empresa`
--

CREATE TABLE `empresa` (
  `id_empresa` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `empresa`
--

INSERT INTO `empresa` (`id_empresa`, `nome`) VALUES
(1, 'GOL'),
(2, 'Avianca'),
(3, 'AZUL'),
(4, 'PANAM'),
(5, 'Emirates');

-- --------------------------------------------------------

--
-- Estrutura para tabela `estado`
--

CREATE TABLE `estado` (
  `id_estado` int(11) NOT NULL,
  `uf` char(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `estado`
--

INSERT INTO `estado` (`id_estado`, `uf`) VALUES
(1, 'RS'),
(2, 'SC'),
(3, 'RN'),
(4, 'SP'),
(5, 'RJ');

-- --------------------------------------------------------

--
-- Estrutura para tabela `modelo`
--

CREATE TABLE `modelo` (
  `id_modelo` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `capacidade` int(250) NOT NULL,
  `combustivel` float NOT NULL,
  `peso` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `modelo`
--

INSERT INTO `modelo` (`id_modelo`, `nome`, `capacidade`, `combustivel`, `peso`) VALUES
(1, 'ASD-3423', 250, 1000, 1000),
(2, 'ASD-3421', 100, 1000, 1000),
(3, 'DSDS-34E323', 50, 1000.1, 1000.1),
(4, 'BTREAVEE', 130, 2000, 2000),
(5, 'GFE-34232', 110, 30000, 30000);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tecnico`
--

CREATE TABLE `tecnico` (
  `id_tecnico` int(11) NOT NULL,
  `codigo` int(11) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefone` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `tecnico`
--

INSERT INTO `tecnico` (`id_tecnico`, `codigo`, `nome_completo`, `email`, `telefone`) VALUES
(6, 1, 'Lucas Fernandes Oliveira', 'lucas@hotmail.com', 51999999999),
(7, 2, 'Marcelo Souza Vieira', 'Marcelo@hotmail.com', 51888888888),
(8, 3, 'Luisa Castro Alves', 'Luisa@hotmail.com', 51777777777),
(9, 4, 'Yuri Ribamar Monchuieve', 'Yuri@gmail.com', 51666666666),
(10, 5, 'William Bonner da Silva', 'William@hotmail.com', 51555555555);

-- --------------------------------------------------------

--
-- Estrutura para tabela `tecnico_modelo`
--

CREATE TABLE `tecnico_modelo` (
  `cod_tecnico` int(11) NOT NULL,
  `cod_modelo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `tecnico_modelo`
--

INSERT INTO `tecnico_modelo` (`cod_tecnico`, `cod_modelo`) VALUES
(6, 1),
(6, 2),
(7, 1),
(8, 3),
(9, 4);

-- --------------------------------------------------------

--
-- Estrutura para tabela `voo`
--

CREATE TABLE `voo` (
  `id_voo` int(11) NOT NULL,
  `horario_partida` datetime NOT NULL,
  `horario_chegada` datetime NOT NULL,
  `cod_aviao` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `voo`
--

INSERT INTO `voo` (`id_voo`, `horario_partida`, `horario_chegada`, `cod_aviao`) VALUES
(1, '2024-05-04 09:00:00', '2024-05-05 12:30:00', 1),
(2, '2024-05-04 09:00:00', '2024-05-05 12:30:00', 2),
(3, '2023-03-02 01:20:00', '2024-03-04 03:45:00', 3),
(4, '2024-05-04 03:00:00', '2024-05-04 04:00:00', 4),
(5, '2024-05-04 09:00:00', '2024-05-05 15:10:00', 5);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `aeroporto`
--
ALTER TABLE `aeroporto`
  ADD PRIMARY KEY (`id_aeroporto`);

--
-- Índices de tabela `aviao`
--
ALTER TABLE `aviao`
  ADD PRIMARY KEY (`id_aviao`),
  ADD UNIQUE KEY `prefixo` (`prefixo`),
  ADD KEY `cod_modelo` (`cod_modelo`),
  ADD KEY `cod_empresa` (`cod_empresa`);

--
-- Índices de tabela `cidade`
--
ALTER TABLE `cidade`
  ADD PRIMARY KEY (`id_cidade`);

--
-- Índices de tabela `empregados`
--
ALTER TABLE `empregados`
  ADD PRIMARY KEY (`id_empregados`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `cod_cidade` (`cod_cidade`),
  ADD KEY `cod_estado` (`cod_estado`);

--
-- Índices de tabela `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id_empresa`);

--
-- Índices de tabela `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id_estado`);

--
-- Índices de tabela `modelo`
--
ALTER TABLE `modelo`
  ADD PRIMARY KEY (`id_modelo`);

--
-- Índices de tabela `tecnico`
--
ALTER TABLE `tecnico`
  ADD PRIMARY KEY (`id_tecnico`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Índices de tabela `tecnico_modelo`
--
ALTER TABLE `tecnico_modelo`
  ADD KEY `cod_tecnico` (`cod_tecnico`),
  ADD KEY `cod_modelo` (`cod_modelo`);

--
-- Índices de tabela `voo`
--
ALTER TABLE `voo`
  ADD PRIMARY KEY (`id_voo`),
  ADD KEY `cod_aviao` (`cod_aviao`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `aeroporto`
--
ALTER TABLE `aeroporto`
  MODIFY `id_aeroporto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `aviao`
--
ALTER TABLE `aviao`
  MODIFY `id_aviao` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `cidade`
--
ALTER TABLE `cidade`
  MODIFY `id_cidade` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `empregados`
--
ALTER TABLE `empregados`
  MODIFY `id_empregados` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id_empresa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `estado`
--
ALTER TABLE `estado`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `modelo`
--
ALTER TABLE `modelo`
  MODIFY `id_modelo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `tecnico`
--
ALTER TABLE `tecnico`
  MODIFY `id_tecnico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `voo`
--
ALTER TABLE `voo`
  MODIFY `id_voo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `aviao`
--
ALTER TABLE `aviao`
  ADD CONSTRAINT `aviao_ibfk_1` FOREIGN KEY (`cod_modelo`) REFERENCES `modelo` (`id_modelo`),
  ADD CONSTRAINT `aviao_ibfk_2` FOREIGN KEY (`cod_empresa`) REFERENCES `empresa` (`id_empresa`);

--
-- Restrições para tabelas `empregados`
--
ALTER TABLE `empregados`
  ADD CONSTRAINT `empregados_ibfk_1` FOREIGN KEY (`cod_cidade`) REFERENCES `cidade` (`id_cidade`),
  ADD CONSTRAINT `empregados_ibfk_2` FOREIGN KEY (`cod_estado`) REFERENCES `estado` (`id_estado`);

--
-- Restrições para tabelas `tecnico_modelo`
--
ALTER TABLE `tecnico_modelo`
  ADD CONSTRAINT `tecnico_modelo_ibfk_1` FOREIGN KEY (`cod_tecnico`) REFERENCES `tecnico` (`id_tecnico`),
  ADD CONSTRAINT `tecnico_modelo_ibfk_2` FOREIGN KEY (`cod_modelo`) REFERENCES `modelo` (`id_modelo`);

--
-- Restrições para tabelas `voo`
--
ALTER TABLE `voo`
  ADD CONSTRAINT `voo_ibfk_1` FOREIGN KEY (`cod_aviao`) REFERENCES `aviao` (`id_aviao`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
