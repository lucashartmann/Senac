<?php

class Pessoa
{
    private String $nome;
    private String $sobrenome;
    private int $idade;
    public String $email;

    public function __construct(String $nome, String $sobrenome, int $idade)
    {
        $this->nome = $nome;
        $this->sobrenome = $sobrenome;
        $this->idade = $idade;
        $this->email = "";
    }

    public function getEmail(): String
    {
        return $this->email;
    }

    public function setEmail(String $email): self
    {
        $this->email = $email;

        return $this;
    }

    public function getNome(): String
    {
        return $this->nome;
    }

    public function setNome(String $nome): self
    {
        $this->nome = $nome;

        return $this;
    }

    public function getSobrenome(): String
    {
        return $this->sobrenome;
    }

    public function setSobrenome(String $sobrenome): self
    {
        $this->sobrenome = $sobrenome;

        return $this;
    }

    public function getIdade(): int
    {
        return $this->idade;
    }

    public function setIdade(int $idade): self
    {
        $this->idade = $idade;

        return $this;
    }

    public function __toString(): String
    {
        return "<p>Nome: " . $this->getNome() . "</p>" .
            "<p>Sobrenome: " . $this->getSobrenome() . "</p>" .
            "<p>Idade: " . $this->getIdade() . "</p>" .
            "<p>Email: " . $this->getEmail() . "</p>";
    }
}
