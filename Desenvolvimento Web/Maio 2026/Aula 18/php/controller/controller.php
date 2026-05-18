<?php


session_start();

include_once '../database/conexaoBanco.php';
include_once '../model/usuario.php';

$login = isset($_POST['usuario']) ? ($_POST['usuario'] ?? '') : '';
$senha = isset($_POST['senha']) ? ($_POST['senha'] ?? '') : '';

$conexao = ConexaoBanco::getInstancia();
$sql = $conexao->prepare("SELECT * FROM usuarios WHERE login = ? AND senha = ?");
$sql->execute(
    [$login, $senha]
);
$dados = $sql->fetch();
if ($dados) {
    $usuario = new Usuario();
    $usuario->setLogin($dados['login']);
    $usuario->setPerfil($dados['perfil']);
    $_SESSION['usuario_logado'] = serialize($usuario);
    if ($usuario->getPerfil() == 'admin') {
        header("Location:../view/dashboard.php");
    }else {
        header("Location:../view/resposta.php");
    }
}else {
    header("Location:../../index.php?erro=1");
}
