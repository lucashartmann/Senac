<?php

include_once '../database/conexaoBanco.php';
include_once 'talento.php';

class TalentoDAO
{
    private $conexao;

    public function __construct()
    {
        $this->conexao = ConexaoBanco::getInstancia();
    }

    public function atualizarCurriculo($id, $nomeArquivo)
    {
        try {
            $sql = $this->conexao->prepare("UPDATE talentos SET curriculo = :curriculo WHERE idTalento = :id");
            $sql->bindValue(':curriculo', $nomeArquivo);
            $sql->bindValue(':id', $id);
            return $sql->execute();
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao atualizar currículo. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }

    public function atualizar($talento)
    {
        try {
            $sql = $this->conexao->prepare("UPDATE talentos SET nome = :nome, email = :email, fone = :fone, tecnologia = :tecnologia WHERE idTalento = :id");
            $sql->bindValue(':nome', $talento->getNome());
            $sql->bindValue(':email', $talento->getEmail());
            $sql->bindValue(':fone', $talento->getFone());
            $sql->bindValue(':tecnologia', $talento->getTecnologia());
            $sql->bindValue(':id', $talento->getId());
            return $sql->execute();
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao atualizar talento. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }

    public function excluir($id)
    {
        try {
            $sql = $this->conexao->prepare("DELETE FROM talentos WHERE idTalento = :id");
            $sql->bindValue(':id', $id);
            return $sql->execute();
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao excluir talento. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }

    public function buscarPorId($id)
    {
        try {
            $sql = $this->conexao->prepare("SELECT * FROM talentos WHERE idTalento = :id");
            $sql->bindValue(':id', $id);
            $sql->execute();
            $dados = $sql->fetch(PDO::FETCH_ASSOC);
            if ($dados) {
                $talento = new Talento();
                $talento->setId($dados['idTalento'] ?? 0);
                $talento->setNome($dados['nome'] ?? '');
                $talento->setEmail($dados['email'] ?? '');
                $talento->setFone($dados['fone'] ?? '');
                $talento->setTecnologia($dados['tecnologia'] ?? '');
                $talento->setSenha($dados['senha'] ?? '');
                $talento->setCurriculo($dados['curriculo'] ?? '');
                return $talento;
            }
            return null;
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao buscar talento por ID. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }

    public function buscarPorFiltro($filtro)
    {
        try {
            $sql = $this->conexao->query("SELECT * FROM talentos WHERE nome LIKE '%$filtro%' OR email LIKE '%$filtro%' OR fone LIKE '%$filtro%' OR tecnologia LIKE '%$filtro%' ORDER BY nome ASC");
            $dados = $sql->fetchAll(PDO::FETCH_ASSOC);
            $talentos = [];
            foreach ($dados as $dado) {
                $talento = new Talento();
                $talento->setId($dado['idTalento'] ?? 0);
                $talento->setNome($dado['nome'] ?? '');
                $talento->setEmail($dado['email'] ?? '');
                $talento->setFone($dado['fone'] ?? '');
                $talento->setTecnologia($dado['tecnologia'] ?? '');
                $talento->setSenha($dado['senha'] ?? '');
                $talento->setCurriculo($dado['curriculo'] ?? '');
                $talentos[] = $talento;
            }
            return $talentos;
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao listar todos os talentos. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
            // return [];
        }
    }

    public function cadastrar($talento)
    {
        try {
            $sql = $this->conexao->prepare("INSERT INTO talentos (nome, email, fone, tecnologia) VALUES (:nome, :email, :fone, :tecnologia)");
            $sql->bindValue(':nome', $talento->getNome());
            $sql->bindValue(':email', $talento->getEmail());
            $sql->bindValue(':fone', $talento->getFone());
            $sql->bindValue(':tecnologia', $talento->getTecnologia());
            return $sql->execute();
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao cadastrar talento. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }

    public function listarTodos()
    {
        try {
            $sql = $this->conexao->query("SELECT * FROM talentos ORDER BY nome ASC");
            $dados = $sql->fetchAll(PDO::FETCH_ASSOC);
            $talentos = [];
            foreach ($dados as $dado) {
                $talento = new Talento();
                $talento->setId($dado['idTalento'] ?? 0);
                $talento->setNome($dado['nome'] ?? '');
                $talento->setEmail($dado['email'] ?? '');
                $talento->setFone($dado['fone'] ?? '');
                $talento->setTecnologia($dado['tecnologia'] ?? '');
                $talento->setSenha($dado['senha'] ?? '');
                $talento->setCurriculo($dado['curriculo'] ?? '');
                $talentos[] = $talento;
            }
            return $talentos;
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao listar todos os talentos. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
            // return [];
        }
    }

    public function verificarLogin($email, $senha)
    {
        try {
            $sql = $this->conexao->prepare("SELECT * FROM talentos WHERE email = :email AND senha = :senha");
            $sql->bindValue(':email', $email);
            $sql->bindValue(':senha', $senha);
            $sql->execute();
            $dados = $sql->fetch(PDO::FETCH_ASSOC);
            if ($dados) {
                $talento = new Talento();
                $talento->setId($dados['idTalento'] ?? 0);
                $talento->setNome($dados['nome'] ?? '');
                $talento->setEmail($dados['email'] ?? '');
                $talento->setFone($dados['fone'] ?? '');
                $talento->setTecnologia($dados['tecnologia'] ?? '');
                $talento->setSenha($dados['senha'] ?? '');
                $talento->setCurriculo($dados['curriculo'] ?? '');
                return $talento;
            }
            return null;
        } catch (PDOException $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao verificar login. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }
}
