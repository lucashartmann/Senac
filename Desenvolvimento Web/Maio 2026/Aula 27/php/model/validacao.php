<?php

class Validacao
{
    public static function validarNome($nome)
    {
        $nome = trim($nome);
        $regex = '//';
        return preg_match($regex, $nome);
    }

    public static function validarEmail($email)
    {
        $email = trim($email);
        $regex = '/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/';
        return preg_match($regex, $email);
    }

    public static function validarTelefone($telefone)
    {
        $telefone = trim($telefone);
        $regex = '/^(\(?\d{2}\)?\s?)?(\d{4,5}\-\d{4}|\d{8,11})$/';
        return preg_match($regex, $telefone);
    }

    public static function validarTecnologias($tecnologias)
    {
        $tecnologias = trim($tecnologias);
        $regex = '//';
        return preg_match($regex, $tecnologias);
    }

    public static function validarSenha($senha)
    {
        // $senha = trim($senha);
        $regex = '/^(?=.*[A-Z])(?=.*[a-z])(?-.*\d).{8,}$/';
        return preg_match($regex, $senha);
    }
}
