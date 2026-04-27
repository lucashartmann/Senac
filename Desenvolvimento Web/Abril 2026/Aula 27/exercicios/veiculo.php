<?php

class Veiculo 
{

    private $marca;
    private $modelo;

    public function __construct($marca, $modelo) {
        $this->marca = $marca;
        $this->modelo = $modelo;
    }

    public function getMarca() {
        return $this->marca;
    }

    public function getModelo() {
        return $this->modelo;
    }

    public function exibirDados() {
        return 'Este veiculo é um ' . $this->marca . " " . $this->modelo; 
    }

}