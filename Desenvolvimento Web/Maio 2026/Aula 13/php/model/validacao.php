<?php
// date_default_timezone_set('America/Sao_Paulo');

class Validacao
{

    public function __construct() {}

    public static function validarNome($nome)
    {
        return !empty($nome) && strlen($nome) >= 3;
    }

    public  static  function validarEmail($email)
    {
        return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
    }

    public static function validarIdade($idade)
    {
        return $idade >= 18 && $idade <= 120;
    }

    public static function validarTech($tech)
    {
        return !empty($tech) && !is_numeric($tech) && strlen($tech) >= 1;
    }

    public static function converterTech($tech)
    {
        try { 
            $tech = trim($tech);
            $tech_convertida = explode(",", $tech);
            sort($tech_convertida, SORT_DESC);
            return $tech_convertida;
        } catch (Exception) {
            return [];
        }
    }
}
