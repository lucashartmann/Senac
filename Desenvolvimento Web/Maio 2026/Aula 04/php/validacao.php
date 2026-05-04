<?php

class Validacao {

    private $REGEX_EMAIL = "/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/";

    private $REGEX_SENHA = "/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/";

    public function validar(string $expressao, string $valor) {
        if ($expressao === 'email') {
            $expressao = $this->REGEX_EMAIL;
        } else if ($expressao === 'senha') {
            $expressao = $this->REGEX_SENHA;
        }
        if (preg_match($expressao, $valor)) {
            return true;
        } else {
            return false;
        }
    }
}
