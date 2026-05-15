<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/usuario.php";

!Segurança::verificarAcesso();

$usuario = unserialize($_SESSION['usuario_logado']);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../../css/dashboard.css">
</head>

<body>
    <div id="wrapper">
        <div class="container">
            <div class="post">
                <h2>Painel de controle administrativo</h2>
                <p>Olá, <strong> <?php echo $usuario->getLogin(); ?>!</strong>. Seu acesso foi validado com sucesso <span style="color: #58a6ff; font-weight: bold;"><?php echo strtoupper($usuario->getPerfil()); ?></span></p>
                <a href="..controller/logout.php">Sair</a>
            </div>
        </div>
    </div>
</body>

</html>