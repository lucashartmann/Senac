<?php

// class Enum {
//     ESTAGIARIO -> "Estagiário";
//     JUNIOR = "Júnior";
//     PLENO_SENIOR = "Pleno/Sênior";
// }
date_default_timezone_set('America/Sao_Paulo');

class Candidato
{
    private $nome;
    private $email;
    private $idade;
    private $tech;
    private $pontos;
    private $classificacao;
    private $dataInscricao;
    

    public function __construct($nome, $email, $idade)
    {
        $this->nome = $nome;
        $this->idade = $idade;
        $this->tech = [];
        $this->email = $email;
        $this->pontos = 0;
        $this->classificacao = "Não classificado";
        $this->dataInscricao = new DateTime("now");
    }

    public function getDataInscricao() {
        return $this->dataInscricao;
    }

    /**
     * Get the value of nome
     */
    public function getNome()
    {
        return $this->nome;
    }

    /**
     * Set the value of nome
     */
    public function setNome($nome): self
    {
        $this->nome = $nome;

        return $this;
    }

    /**
     * Get the value of email
     */
    public function getEmail()
    {
        return $this->email;
    }

    public function getPontos()
    {
        return $this->pontos;
    }

    public function setPontos($pontos): self
    {
        $this->pontos = $pontos;

        return $this;
    }

    public function setClassificacao($classificacao){
        $this->classificacao = $classificacao;
    }

    public function definirClassificacao(){
        if ($this->pontos > 0 && $this->pontos <= 30) $this->setClassificacao("Estagiário");
        else if ($this->pontos <=31) $this->setClassificacao("Estagiário");
        else if ($this->pontos <=60) $this->setClassificacao("Júnior");
        else if ($this->pontos > 60) $this->setClassificacao("Pleno/Sênior");
        else $this->setClassificacao("Não classificado");
    }

    public function calcularPontos() {
        $this->pontos = 0;
        $listaSemDuplicados = array_unique($this->tech, SORT_STRING) ?? [];
        if(count($listaSemDuplicados) < 1) return;
        for ($i = 0; $i < count($this->$listaSemDuplicados); $i++) {
            if ($this->$listaSemDuplicados[$i] == "php" || $this->$listaSemDuplicados[$i] == "rust") {
                $this->pontos+=20;
            }
            else {
                $this->pontos+=10;
            };
        }
    }

    /**
     * Set the value of email
     */
    public function setEmail($email): self
    {
        $this->email = $email;

        return $this;
    }

    /**
     * Get the value of idade
     */
    public function getIdade()
    {
        return $this->idade;
    }

    /**
     * Set the value of idade
     */
    public function setIdade($idade): self
    {
        $this->idade = $idade;

        return $this;
    }

    public function getClassificacao() {
        return $this->classificacao;
    }

    /**
     * Get the value of tech
     */
    public function getTech()
    {
        return $this->tech;
    }

    /**
     * Set the value of tech
     */
    public function setTech($tech): self
    {
        $this->tech = $tech;

        return $this;
    }

    public function __toString()
    {
        return "<h3>Relatório do Candidato</h3>" .
            "<p>Nome: " . ($this->getNome() ? $this->getNome() : "INVÁLIDO") . "</p>" .
            "<p>E-mail: " . ($this->getEmail() ? ucfirst($this->getEmail()) : "INVÁLIDO") . "</p>" .
            "<p>Idade: " . ($this->getIdade() ? $this->getIdade() . " anos" : "Idade fora do padrão") . "</p>" .
            "<p>Total de Tecnologias: " . ($this->getTech() ? count($this->getTech()) : 0) . "</p>" .
            "<p>Lista de Techs: " . ($this->getTech() ? htmlspecialchars(implode(" | ", $this->getTech())) : "Nenhuma tecnologia registrada") . "</p>" . 
            "<p>Pontuação: " . $this->getPontos() . "</p>" .
            "<p>Classificação: " . $this->getClassificacao() . "</p>" .
            "<p>Data de cadastro: " . date_format($this->getDataInscricao(), "d/m/y") .  "</p>";
    }
}
