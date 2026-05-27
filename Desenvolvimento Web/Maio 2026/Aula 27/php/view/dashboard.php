<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/usuario.php";

Segurança::verificarAcesso();

$usuario = unserialize($_SESSION['usuario_logado']);
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/dashboard.css">
</head>

<body>
    <div id="wrapper">
        <div class="container">
            <h2>Painel de controle administrativo</h2>

            <p>Olá, <strong> <?php echo $usuario->getLogin(); ?>!</strong>. Seu acesso foi validado com sucesso <span style="color: #58a6ff; font-weight: bold;"><?php echo strtoupper($usuario->getPerfil()); ?></span></p>

            <hr style="border:0; border-top: 1px solid #30363d; margin: 20px 0;">
            <div class="post">
                <ul>
                    <li>
                        <a href="../view/cadastro.php" class="btn">Cadastrar Talento</a>
                    </li>
                    <li>
                        <a href="../view/consultaTalentos.php" class="btn">Consultar Talentos</a>
                    </li>
                </ul>
                <a href="../controller/controller.php?acao=deslogar" style="color:#ff7b72;">Sair</a>
            </div>


        </div>
        <footer>
            
            <p>&copy; 2026 Lucas Augusto. Todos os direitos reservados.</p>
        </footer>

    </div>
</body>

</html>