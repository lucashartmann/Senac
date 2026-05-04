
<?php

include_once 'validacao.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header("Location: view.php?mensagem=Requisição inválida");
    exit();
}

$email = $_POST['email'];
$senha = $_POST['senha'];

$validacao = new Validacao();

if ($validacao->validar('email', $email) && $validacao->validar('senha', $senha)) {
    header("Location: view.php?mensagem=Login realizado com sucesso&email=$email&senha=$senha");
} else if (!$validacao->validar('email', $email)) {
    header("Location: view.php?mensagem=Email inválido&email=$email&senha=$senha");
} else if (!$validacao->validar('senha', $senha)) {
    header("Location: view.php?mensagem=Senha inválida&email=$email&senha=$senha");
}