-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 21/03/2025 às 14:18
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
-- Estrutura para tabela `clientes`
--

CREATE TABLE `clientes` (
  `id_clientes` int(11) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `data_nasc` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `clientes`
--

INSERT INTO `clientes` (`id_clientes`, `nome_completo`, `endereco`, `cpf`, `data_nasc`) VALUES
(1, 'Roberslindo da Silva', 'Av. Maria Santa 11', '11111111111', '2003-07-05'),
(2, 'Juriscreide Fernandes', 'Av. Julio Pereira 1999', '22222222222', '1999-03-04'),
(3, 'Teresa Fagundes', 'Santa Terezinha 22', '33333333333', '1989-12-11'),
(4, 'Kelvin Cristo', 'Marcelo Teireixa 123', '44444444444', '1992-09-04'),
(5, 'Leonara Ambos', 'Av. Maria Santa 900', '55555555555', '2003-03-02');

-- --------------------------------------------------------

--
-- Estrutura para tabela `corridas`
--

CREATE TABLE `corridas` (
  `id_corridas` int(11) NOT NULL,
  `origem` varchar(100) NOT NULL,
  `destino` varchar(100) NOT NULL,
  `data_corrida` date NOT NULL,
  `codigo_motorista` int(11) NOT NULL,
  `codigo_cliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `corridas`
--

INSERT INTO `corridas` (`id_corridas`, `origem`, `destino`, `data_corrida`, `codigo_motorista`, `codigo_cliente`) VALUES
(1, 'Av. Maria Santa 11', 'Av. Julio Pereira 1999', '2025-01-02', 1, 1),
(2, 'Av. Julio Pereira 1999', 'Av. Maria Santa 11', '2024-05-06', 1, 2),
(3, 'Santa Terezinha 22', 'Av. Maria Santa 900', '2021-03-04', 3, 3),
(4, 'Marcelo Teireixa 123', 'Santa Terezinha 22', '2024-12-03', 4, 4),
(5, 'Av. Maria Santa 900', 'Marcelo Teireixa 123', '2019-10-12', 5, 5);

-- --------------------------------------------------------

--
-- Estrutura para tabela `mecanicos`
--

CREATE TABLE `mecanicos` (
  `id_mecanicos` int(11) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `celular` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `mecanicos`
--

INSERT INTO `mecanicos` (`id_mecanicos`, `nome_completo`, `endereco`, `cidade`, `estado`, `cpf`, `celular`) VALUES
(1, 'Lucas de Abreu', 'Lima e Silva 255', 'Porto Alegre', 'Rio Grande do Sul', '11111111111', 51111111111),
(2, 'Marcelo Teixeira Lima', 'Venâncio Aires 99', 'Porto Alegre', 'Rio Grande do Sul', '22222222222', 51222222222),
(3, 'Sandra Abulquerque', 'Travessa Ferreira de Abreu 11', 'Blumenau', 'Santa Catarina', '33333333333', 51333333333),
(4, 'Fernanda Lima da Silva', 'Zélia Maria 22', 'Lajeado', 'Rio Grande do Sul', '44444444444', 51444444444),
(5, 'Rosângela Santos', 'Distrito 13', 'Encantado', 'Rio Grande do Sul', '55555555555', 51555555555);

-- --------------------------------------------------------

--
-- Estrutura para tabela `motoristas`
--

CREATE TABLE `motoristas` (
  `id_motoristas` int(11) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `categoria_carteira` char(1) NOT NULL,
  `numero_carteira` int(11) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `endereco` varchar(100) NOT NULL,
  `cidade` varchar(100) NOT NULL,
  `estado` varchar(100) NOT NULL,
  `celular` bigint(11) NOT NULL,
  `codigo_carro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `motoristas`
--

INSERT INTO `motoristas` (`id_motoristas`, `nome_completo`, `categoria_carteira`, `numero_carteira`, `cpf`, `endereco`, `cidade`, `estado`, `celular`, `codigo_carro`) VALUES
(1, 'Leonardo Hoffman', 'A', 2147483647, '66666666666', 'Av. Bento Gonçalves 61', 'Porto Alegre', 'Rio Grande do Sul', 51111111111, 5),
(2, 'Miguel Fernandes', 'B', 2147483647, '11111111111', 'Hélio Penha 122', 'Jurere', 'Santa Catarina', 51555555555, 4),
(3, 'William Marcelo', 'C', 2147483647, '77777777777', 'Luiz Gonçalves 99', 'Anta Gorda', 'Rio Grande do Sul', 51444444444, 3),
(4, 'Christopher Junior Eduardo', 'A', 2147483647, '88888888888', 'Teixeira Neves 44', 'Não-Me-Toque', 'Rio Grande do Sul', 51333333333, 2),
(5, 'Yuri Echevarria', 'B', 2147483647, '99999999999', 'Fernandes Vieira 4000', 'Porto Alegre', 'Rio Grande do Sul', 51222222222, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `servicos`
--

CREATE TABLE `servicos` (
  `id_servicos` int(11) NOT NULL,
  `data_solicitacao` date NOT NULL,
  `data_problema` date NOT NULL,
  `descricao_problema` text DEFAULT NULL,
  `codigo_veiculo` int(11) NOT NULL,
  `codigo_motorista` int(11) NOT NULL,
  `codigo_mecanico` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `servicos`
--

INSERT INTO `servicos` (`id_servicos`, `data_solicitacao`, `data_problema`, `descricao_problema`, `codigo_veiculo`, `codigo_motorista`, `codigo_mecanico`) VALUES
(1, '2024-02-05', '2024-01-05', NULL, 1, 1, 1),
(2, '2025-02-05', '2024-11-12', NULL, 3, 3, 3),
(3, '2024-02-05', '2024-01-05', NULL, 4, 4, 4),
(4, '2025-02-02', '2025-01-01', NULL, 5, 5, 5),
(5, '2023-02-05', '2023-01-02', 'Carburador com defeito', 2, 2, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `veiculos`
--

CREATE TABLE `veiculos` (
  `id_veiculos` int(11) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `placa` varchar(7) NOT NULL,
  `ano_fabricacao` int(4) NOT NULL,
  `numero_chassi` varchar(17) NOT NULL,
  `cor` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Despejando dados para a tabela `veiculos`
--

INSERT INTO `veiculos` (`id_veiculos`, `marca`, `modelo`, `placa`, `ano_fabricacao`, `numero_chassi`, `cor`) VALUES
(1, 'Chevrolet', 'Trailblazer', 'AGF1934', 2008, 'AS20339581H583J43', 'Vermelho'),
(2, 'Fiat', 'Uno', 'AGF1934', 2009, 'AS20339581H583J42', 'Verde'),
(3, 'Chevrolet', 'Camaro', 'AGF1934', 2010, 'AS20339581H583J41', 'Laranja'),
(4, 'Renault', 'Civic', 'AGF1934', 2011, 'AS20339581H583J40', 'Rosa'),
(5, 'Fiat', 'Tipo', 'AGF1934', 2012, 'AS20339581H583J31', 'Azul');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_clientes`);

--
-- Índices de tabela `corridas`
--
ALTER TABLE `corridas`
  ADD PRIMARY KEY (`id_corridas`),
  ADD KEY `codigo_cliente` (`codigo_cliente`),
  ADD KEY `codigo_motorista` (`codigo_motorista`);

--
-- Índices de tabela `mecanicos`
--
ALTER TABLE `mecanicos`
  ADD PRIMARY KEY (`id_mecanicos`);

--
-- Índices de tabela `motoristas`
--
ALTER TABLE `motoristas`
  ADD PRIMARY KEY (`id_motoristas`),
  ADD KEY `codigo_carro` (`codigo_carro`);

--
-- Índices de tabela `servicos`
--
ALTER TABLE `servicos`
  ADD PRIMARY KEY (`id_servicos`),
  ADD KEY `codigo_veiculo` (`codigo_veiculo`),
  ADD KEY `codigo_motorista` (`codigo_motorista`),
  ADD KEY `codigo_mecanico` (`codigo_mecanico`);

--
-- Índices de tabela `veiculos`
--
ALTER TABLE `veiculos`
  ADD PRIMARY KEY (`id_veiculos`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_clientes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `corridas`
--
ALTER TABLE `corridas`
  MODIFY `id_corridas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `mecanicos`
--
ALTER TABLE `mecanicos`
  MODIFY `id_mecanicos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `motoristas`
--
ALTER TABLE `motoristas`
  MODIFY `id_motoristas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `servicos`
--
ALTER TABLE `servicos`
  MODIFY `id_servicos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `veiculos`
--
ALTER TABLE `veiculos`
  MODIFY `id_veiculos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `corridas`
--
ALTER TABLE `corridas`
  ADD CONSTRAINT `corridas_ibfk_1` FOREIGN KEY (`codigo_cliente`) REFERENCES `clientes` (`id_clientes`),
  ADD CONSTRAINT `corridas_ibfk_2` FOREIGN KEY (`codigo_motorista`) REFERENCES `veiculos` (`id_veiculos`);

--
-- Restrições para tabelas `motoristas`
--
ALTER TABLE `motoristas`
  ADD CONSTRAINT `motoristas_ibfk_1` FOREIGN KEY (`codigo_carro`) REFERENCES `veiculos` (`id_veiculos`);

--
-- Restrições para tabelas `servicos`
--
ALTER TABLE `servicos`
  ADD CONSTRAINT `servicos_ibfk_1` FOREIGN KEY (`codigo_veiculo`) REFERENCES `veiculos` (`id_veiculos`),
  ADD CONSTRAINT `servicos_ibfk_2` FOREIGN KEY (`codigo_motorista`) REFERENCES `motoristas` (`id_motoristas`),
  ADD CONSTRAINT `servicos_ibfk_3` FOREIGN KEY (`codigo_mecanico`) REFERENCES `mecanicos` (`id_mecanicos`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
