<?php

class Candidato {
    private $nome;
    private $email;
    private $idade;
    private $tech;

    public function __construct($nome, $email, $idade) {
        $this->nome = $nome;
        $this->idade = $idade;
        $this->tech = "";
        $this->email = $email;
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

    public __toString() {
        echo `
            <p>Nome:${$this->nome}</p>
            <p>Idade:</p>
            <p>Email:</p>
            <p>Techs: </p>
        `
    }
}