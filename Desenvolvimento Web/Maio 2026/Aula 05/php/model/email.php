<?php

class Email {
    private $destinatario;
    private $assunto;
    private $mensagem;

    public function __construct($mensagem) {
        $this->destinatario = "05725184048@senacrs.edu.br";
        $this->assunto = "Contato via site";    
        $this->mensagem = $mensagem;
    }

    public function getDestinatario() {
        return $this->destinatario;
    }

    public function getAssunto() {
        return $this->assunto;
    }

    public function getMensagem() {
        return $this->mensagem;
    }

    public function setDestinatario($destinatario) {
        $this->destinatario = $destinatario;
    }

    public function enviarEmail() {
        return mail($this->destinatario, $this->assunto, $this->mensagem);
    }
}