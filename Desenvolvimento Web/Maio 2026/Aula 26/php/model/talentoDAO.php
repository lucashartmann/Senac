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
        } catch (Exception $e) {
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
        } catch (Exception $e) {
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
            return $sql->fetch(PDO::FETCH_ASSOC);
        } catch (Exception $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao buscar talento por ID. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }

    public function buscarPorFiltro($filtro)
    {
        try {
            $sql = $this->conexao->query("SELECT * FROM talentos WHERE nome LIKE '%$filtro%' OR email LIKE '%$filtro%' OR fone LIKE '%$filtro%' OR tecnologia LIKE '%$filtro%' ORDER BY nome ASC");
            return $sql->fetchAll(PDO::FETCH_ASSOC);
        } catch (Exception $e) {
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
        } catch (Exception $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao cadastrar talento. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
        }
    }

    public function listarTodos()
    {
        try {
            $sql = $this->conexao->query("SELECT * FROM talentos ORDER BY nome ASC");
            return $sql->fetchAll(PDO::FETCH_ASSOC);
        } catch (Exception $e) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao listar todos os talentos. " . $e->getMessage() . "</p>";
            header("Location: ../view/erro.php");
            exit;
            // return [];
        }
    }
}
