-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 20-Mar-2025 às 02:26
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

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
-- Estrutura da tabela `aluno`
--

CREATE TABLE `aluno` (
  `num_matri` int(11) NOT NULL,
  `data_nasci` date NOT NULL,
  `rua` varchar(100) NOT NULL,
  `bairro` varchar(50) NOT NULL,
  `cep` varchar(9) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `genero` char(1) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `aluno`
--

INSERT INTO `aluno` (`num_matri`, `data_nasci`, `rua`, `bairro`, `cep`, `cidade`, `genero`, `nome`) VALUES
(10006, '2001-02-15', 'Rua dos Estudantes, 101', 'Centro', '01234-568', 'São Paulo', 'M', 'Lucas Silva'),
(10007, '2001-05-22', 'Av. das Universidades, 201', 'Pinheiros', '02345-679', 'São Paulo', 'F', 'Camila Oliveira'),
(10008, '1998-10-10', 'Rua Doutor Silva, 301', 'Saúde', '03456-790', 'São Paulo', 'M', 'Felipe Almeida'),
(10009, '2003-03-28', 'Av. Paulista, 401', 'Bela Vista', '04567-891', 'São Paulo', 'F', 'Laura Souza'),
(10010, '2001-10-17', 'Rua da Tecnologia, 501', 'Vila Mariana', '05678-902', 'São Paulo', 'M', 'Tiago Ferreira');

-- --------------------------------------------------------

--
-- Estrutura da tabela `cursos`
--

CREATE TABLE `cursos` (
  `id_cursos` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `turno` varchar(20) NOT NULL,
  `area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `cursos`
--

INSERT INTO `cursos` (`id_cursos`, `nome`, `turno`, `area`) VALUES
(1, 'Engenharia de Computação', 'Manhã', 'Tecnologia'),
(2, 'Gestão Empresarial', 'Noite', 'Negócios'),
(3, 'Medicina Veterinária', 'Integral', 'Saúde'),
(4, 'Direito Penal', 'Noite', 'Humanas'),
(5, 'Sistemas de Informação', 'Tarde', 'Tecnologia');

-- --------------------------------------------------------

--
-- Estrutura da tabela `dependentes`
--

CREATE TABLE `dependentes` (
  `cod_depe` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `grau_parentesco` varchar(50) NOT NULL,
  `data_nasc` date NOT NULL,
  `cod_doce` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `dependentes`
--

INSERT INTO `dependentes` (`cod_depe`, `nome`, `grau_parentesco`, `data_nasc`, `cod_doce`) VALUES
(1, 'Ana Silva', 'Filha', '2016-03-12', 1),
(2, 'Carlos Oliveira', 'Filho', '2018-07-25', 2),
(3, 'Beatriz Santos', 'Filha', '2011-11-30', 3),
(4, 'Lucas Pereira', 'Filho', '2017-05-18', 4),
(5, 'Renato Lima', 'Filho', '2015-09-22', 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `disciplina`
--

CREATE TABLE `disciplina` (
  `cod_disc` int(11) NOT NULL,
  `descricao` varchar(200) NOT NULL,
  `codigo_sala` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `disciplina`
--

INSERT INTO `disciplina` (`cod_disc`, `descricao`, `codigo_sala`) VALUES
(11, 'Programação Orientada a Objetos', 1),
(12, 'Gestão Empresarial', 2),
(13, 'Anatomia Humana', 3),
(14, 'Direito Constitucional', 4),
(15, 'Estrutura de Dados', 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `docente`
--

CREATE TABLE `docente` (
  `cod_doce` int(11) NOT NULL,
  `endereco` varchar(200) NOT NULL,
  `telefone` bigint(11) NOT NULL,
  `nome` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `docente`
--

INSERT INTO `docente` (`cod_doce`, `endereco`, `telefone`, `nome`) VALUES
(1, 'Rua das Flores, 123', 1122334455, 'Ana Silva'),
(2, 'Av. Principal, 456', 2233445566, 'Carlos Oliveira'),
(3, 'Rua do Comércio, 789', 3344556677, 'Maria Santos'),
(4, 'Av. Brasil, 321', 4455667788, 'João Pereira'),
(5, 'Rua das Palmeiras, 654', 5566778899, 'Fernanda Lima'),
(6, 'Rua das Flores, 123', 1122334455, 'Ana Silva'),
(7, 'Av. Principal, 456', 2233445566, 'Carlos Oliveira'),
(8, 'Rua do Comércio, 789', 3344556677, 'Maria Santos'),
(9, 'Av. Brasil, 321', 4455667788, 'João Pereira'),
(10, 'Rua das Palmeiras, 654', 5566778899, 'Fernanda Lima');

-- --------------------------------------------------------

--
-- Estrutura da tabela `matricula`
--

CREATE TABLE `matricula` (
  `id_matricula` int(11) NOT NULL,
  `data_matri` date NOT NULL,
  `numero_matricula` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `matricula`
--

INSERT INTO `matricula` (`id_matricula`, `data_matri`, `numero_matricula`, `id_curso`) VALUES
(16, '2022-03-10', 10006, 1),
(17, '2022-03-11', 10007, 2),
(18, '2022-03-09', 10008, 3),
(19, '2022-03-12', 10009, 4),
(20, '2022-03-08', 10010, 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `sala`
--

CREATE TABLE `sala` (
  `cod_sala` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `localizacao` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Extraindo dados da tabela `sala`
--

INSERT INTO `sala` (`cod_sala`, `nome`, `localizacao`) VALUES
(1, 'Laboratório de Engenharia de Software', 'Bloco A - Térreo'),
(2, 'Sala de Aula 2', 'Bloco B - 1º Andar'),
(3, 'Auditório Principal', 'Bloco C - Térreo'),
(4, 'Laboratório de Ciências', 'Bloco D - 2º Andar'),
(5, 'Sala de Estudos Avançados', 'Biblioteca - 3º Andar');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `aluno`
--
ALTER TABLE `aluno`
  ADD PRIMARY KEY (`num_matri`);

--
-- Índices para tabela `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_cursos`);

--
-- Índices para tabela `dependentes`
--
ALTER TABLE `dependentes`
  ADD PRIMARY KEY (`cod_depe`),
  ADD KEY `cod_doce` (`cod_doce`);

--
-- Índices para tabela `disciplina`
--
ALTER TABLE `disciplina`
  ADD PRIMARY KEY (`cod_disc`),
  ADD KEY `codigo_sala` (`codigo_sala`);

--
-- Índices para tabela `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`cod_doce`);

--
-- Índices para tabela `matricula`
--
ALTER TABLE `matricula`
  ADD PRIMARY KEY (`id_matricula`),
  ADD KEY `numero_matricula` (`numero_matricula`),
  ADD KEY `id_curso` (`id_curso`);

--
-- Índices para tabela `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`cod_sala`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id_cursos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `dependentes`
--
ALTER TABLE `dependentes`
  MODIFY `cod_depe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `disciplina`
--
ALTER TABLE `disciplina`
  MODIFY `cod_disc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de tabela `docente`
--
ALTER TABLE `docente`
  MODIFY `cod_doce` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `matricula`
--
ALTER TABLE `matricula`
  MODIFY `id_matricula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de tabela `sala`
--
ALTER TABLE `sala`
  MODIFY `cod_sala` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `dependentes`
--
ALTER TABLE `dependentes`
  ADD CONSTRAINT `dependentes_ibfk_1` FOREIGN KEY (`cod_doce`) REFERENCES `docente` (`cod_doce`);

--
-- Limitadores para a tabela `disciplina`
--
ALTER TABLE `disciplina`
  ADD CONSTRAINT `disciplina_ibfk_1` FOREIGN KEY (`codigo_sala`) REFERENCES `sala` (`cod_sala`);

--
-- Limitadores para a tabela `matricula`
--
ALTER TABLE `matricula`
  ADD CONSTRAINT `matricula_ibfk_1` FOREIGN KEY (`numero_matricula`) REFERENCES `aluno` (`num_matri`),
  ADD CONSTRAINT `matricula_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_cursos`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
