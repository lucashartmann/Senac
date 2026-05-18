<?php

include_once '../database/conexaoBanco.php';
include_once 'talento.php';

class TalentoDAO
{
    private $conexao;

    public function __construct($conexao)
    {
        $this->conexao = ConexaoBanco::getInstancia();
    }

    public function cadastrarTalento($talento)
    {
        try {
            $sql = "INSERT INTO talentos (nome, email, fone, tecnologia) VALUES (:nome, :email, :fone, :tecnologia)";
            $stmt = $this->conexao->prepare($sql);
            $stmt->bindValue(':nome', $talento->getNome());
            $stmt->bindValue(':email', $talento->getEmail());
            $stmt->bindValue(':fone', $talento->getFone());
            $stmt->bindValue(':tecnologia', $talento->getTecnologia());
            return $stmt->execute();
        } catch (Exception $e) {
            header("Location: ../view/erro.php?mensagem=Erro ao cadastrar talento.");
            exit;
        }
    }

    public function listarTodos() {
        try {
            $sql = $this->conexao->query("SELECT * FROM talentos ORDER BY nome ASC");
            return $sql->fetchAll(PDO::FETCH_ASSOC);
        }catch (Exception $e) {
            header("Location: ../view/erro.php?mensagem=Erro ao listar todos os talentos.");
            exit;
            // return [];
        }
    }
}
