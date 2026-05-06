<?php

class Validacao 
{
    public static function validarNome($nome) {
        $nome = trim($nome);
        return !empty($nome) && strlen($nome) >= 3 && !is_numeric($nome) && preg_match("/^[a-zA-Z\s]+$/", $nome);
    }

    public static function validarIdade($idade) {
        return is_numeric($idade) && $idade > 0 && $idade < 150;
    }
}