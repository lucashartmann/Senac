<?php

class Segurança {
    public static function verificarAcesso() {
        if (!isset($_SESSION['usuario_logado'])) {
            header("Location:../view/erro.php?mensagem=Acesso Negado! Por favor, realize o login para acessar esta área");
            exit();
        } else {
            return;
        }
    }
}