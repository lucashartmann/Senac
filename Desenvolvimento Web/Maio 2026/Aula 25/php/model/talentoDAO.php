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

    public function atualizar($talento) {
        
    }

    public function excluir($id) {
        try {
            $sql = $this->conexao->prepare("DELETE FROM talentos WHERE idTalento = :id");
            $sql->bindValue(':id', $id);
            return $sql->execute();
        } catch (Exception $e) {
            header("Location: ../view/erro.php?mensagem=Erro ao excluir talento.");
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
            header("Location: ../view/erro.php?mensagem=Erro ao obter talento por ID.");
            exit;
        }
    }

    public function buscarPorFiltro($filtro)
    {
        try {
            $sql = $this->conexao->query("SELECT * FROM talentos WHERE nome LIKE '%$filtro%' OR email LIKE '%$filtro%' OR fone LIKE '%$filtro%' OR tecnologia LIKE '%$filtro%' ORDER BY nome ASC");
            return $sql->fetchAll(PDO::FETCH_ASSOC);
        } catch (Exception $e) {
            header("Location: ../view/erro.php?mensagem=Erro ao listar todos os talentos.");
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
            header("Location: ../view/erro.php?mensagem=Erro ao cadastrar talento.");
            exit;
        }
    }

    public function listarTodos()
    {
        try {
            $sql = $this->conexao->query("SELECT * FROM talentos ORDER BY nome ASC");
            return $sql->fetchAll(PDO::FETCH_ASSOC);
        } catch (Exception $e) {
            header("Location: ../view/erro.php?mensagem=Erro ao listar todos os talentos.");
            exit;
            // return [];
        }
    }
}
