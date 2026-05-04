
<?php

include_once '../model/validacao.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header("Location: ../view/view.php?mensagem=Requisição inválida");
    exit();
}

$email = $_POST['email'];
$senha = $_POST['senha'];

$validacao = new Validacao($email);
$validacao->setSenha($senha);

if ($validacao->validar('email', $email) && $validacao->validar('senha', $senha)) {
    header("Location: ../view/view.php?mensagem=Login realizado com sucesso&validacao=$validacao");
} else if (!$validacao->validar('email', $email)) {
    header("Location: ../view/view.php?mensagem=Email ou Senha inválidos&validacao=$validacao");
} else if (!$validacao->validar('senha', $senha)) {
    header("Location: ../view/view.php?mensagem=Email ou Senha inválidos&validacao=$validacao");
}