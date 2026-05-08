<? 

class Validacao {


    public static function  validarNome($nome) {
    }

    public  static  function validarEmail($email){

    }

    public static function  validarIdade($idade){

    }

    public static function validarTech($tech) {

    }

    public static function converterTech($tech){
        try {
           $tech_convertida = serialize($tech);
           return $tech_convertida;
        }catch(Exception){
            return null;
        }
    }

}