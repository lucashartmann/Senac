<?php

class Usuario {

    private string $login;
    private string $perfil;

    public function __construct()
    {
        
    }

    public function getLogin() {
        return $this->login;
    }

    public function getPerfil(){
        return $this->perfil;
    }

    public function setLogin($login) {
        $this->login = $login;
    }

    public function setPerfil($perfil) {
        $this->perfil = $perfil;
    }

    public function __toString() {
        return "Usuário: {$this->getLogin()} | Perfil: {$this->getPerfil()}";
    }

}