<?php 

class Validacao {

    public static function validarEmail($email) {
        return filter_var($email, FILTER_VALIDATE_EMAIL);
    }

    public static function validarNome($nome) {
        return !empty($nome) && strlen($nome) <= 255;
        // $exp = '/^[a-zA-ZáÁéÉíÍóÓúÚçÇãÃõPêÊ]{2,20}$/';
        // if (preg_match($exp, $nome)) {
        //     return true;
        // } else {
        //     return false;
        // }
    }

    public static function validarTelefone($telefone) {
        return preg_match('/^\d{8,15}$/', $telefone) === 1;
    }
}