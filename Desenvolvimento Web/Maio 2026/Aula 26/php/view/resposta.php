<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/usuario.php";

Segurança::verificarAcesso();

$usuario = unserialize($_SESSION['usuario_logado']);

if (isset($_SESSION['mensagem'])) {
    $mensagem = $_SESSION['mensagem'];
    unset($_SESSION['mensagem']);
}

?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resposta</title>
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/resposta.css">
</head>

<body>
    <div id="wrapper">
        <div class="container">
            <div class="header">
                <h3>Área do Candidato</h3>
                <a href="../controller/controller.php?acao=deslogar">Sair</a>
            </div>
            <hr style="border:0; border-top: 1px solid #30363d; margin: 20px 0;">
            <div class="post">

                <p>Olá, <strong> <?php echo $usuario->getLogin(); ?>!</strong>. Seu acesso foi validado com sucesso <span style="color: #58a6ff; font-weight:bold;"><?php echo strtoupper($usuario->getPerfil()); ?></span></p>

                <hr style="border:0; border-top: 1px solid #30363d; margin: 20px 0;">

                <p style="font-size: 0.9rem; color: #8b949e;">Esta é a tela de resposta padrão para usuários. <br> Seu próximo passo será completar o cadastro de tecnologias.</p>

            </div>
        </div>
        <footer>
            <p>&copy; 2026 Lucas Augusto. Todos os direitos reservados.</p>
        </footer>
    </div>
</body>

</html>