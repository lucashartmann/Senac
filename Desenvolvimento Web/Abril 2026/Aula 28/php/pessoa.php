<?php
class Pessoa {
    private $nome;
    private $sexo;
    private $idade;

    public function __construct($nome, $sexo) {
        $this->nome = $nome;
        $this->sexo = $sexo;
    }

    public function __get($atributo)
    {
        return $this->$atributo;
    }

    public function __set($atributo, $valor)
    {
        $this->$atributo = $valor;
    }

    public function __toString()
    {
        return '<p>nome: ' . $this->nome . '<br>sexo: ' . $this->sexo . '<br>idade: ' . $this->idade . '</p>';
    }

}