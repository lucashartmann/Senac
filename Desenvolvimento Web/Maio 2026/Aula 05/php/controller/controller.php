<?php

include_once '../model/contato.php';
include_once '../model/validacao.php';
include_once '../model/email.php';

$nome = $_POST['nome'];
$email = $_POST['email'];
$telefone = $_POST['telefone'];

$contato_um = new Contato($nome, $email, $telefone);

if (!Validacao::validarNome($contato_um->getNome()) || !Validacao::validarEmail($contato_um->getEmail()) || !Validacao::validarTelefone($contato_um->getTelefone())) {
    header('Location: ../view/erro.php');
    exit();
}

$mensagem = "Nome: " . $contato_um->getNome() . "\nEmail: " . $contato_um->getEmail() . "\nTelefone: " . $contato_um->getTelefone();
$email_obj = new Email($mensagem);
$email_obj->enviarEmail();

header('Location: ../view/resposta.php?nome='.$contato_um->getNome().'&email='.$contato_um->getEmail().'&telefone='.$contato_um->getTelefone());
exit();
