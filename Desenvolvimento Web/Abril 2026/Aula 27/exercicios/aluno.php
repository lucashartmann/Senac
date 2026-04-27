<?php

class Aluno
{
    private $nome;
    private $nota1;
    private $nota2;

    public function __construct($nome)
    {
        $this->nome = $nome;
    }

    public function getNome() {
        return $this->nome;
    }

    public function setNota1($nota1)
    {
        $this->nota1 = $nota1;
    }

    public function setNota2($nota2)
    {
        $this->nota2 = $nota2;
    }

    public function calcularMedia()
    {
        return ($this->nota1 + $this->nota2) / 2;
    }
}
