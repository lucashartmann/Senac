<?php

class Validacao {

    private $email;
    private $senha;
    private $status;

    private $REGEX_EMAIL = "/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/";

    private $REGEX_SENHA = "/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/";

    public function __construct($email) {
        $this->email = $email;
    }

    // public function __set($name, $value) {
    //     $this->$name = $value;
    // }

    // public function __get($name) {
    //     return $this->$name;
    // }

    public function getEmail() {
        return $this->email;
    }

    public function setEmail($email) {
        $this->email = $email;
    }

    public function getSenha() {
        return $this->senha;
    }

    public function setSenha($senha) {
        $this->senha = $senha;
    }

    public function validar(string $expressao, string $valor) {
        if ($expressao === 'email') {
            $expressao = $this->REGEX_EMAIL;
        } else if ($expressao === 'senha') {
            $expressao = $this->REGEX_SENHA;
        }
        if (preg_match($expressao, $valor)) {
            $this->status = "válido";
            return true;
        } else {
            $this->status = "inválido";
            return false;
        }
    }

    public function __toString()
    {
        return "<p>Usuário: " . $this->email . "<br>Status: " . $this->status . "</p>";
    }
}
