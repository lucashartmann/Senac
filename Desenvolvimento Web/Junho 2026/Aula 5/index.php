<?php
session_start();

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
    <title>Sistema Tech Talent - Login</title>
    <link rel="stylesheet" href="css/base.css">
    <link rel="stylesheet" href="css/index.css">
</head>

<body>
    <div id="wrapper">
        <div id="header" class="container">
            <h1>Acesso ao Sistema</h1>
        </div>
        <div id="page" class="container">
            <div id="content">
                <div class="post">
                    <h2 class="title">Login</h2>
                    <?php if (isset($mensagem)) {
                        echo $mensagem;
                    } ?>
                    <form action="php/controller/controller.php?acao=logar" method="POST">
                        <input type="username" name="usuario" placeholder="Digite o nome de usuário" required value="l@email.com">
                        <input type="password" name="senha" placeholder="Digite a senha de acesso" required value="123">
                        <div class="form-actions btn-group">
                            <input type="submit" value="Entrar" class="btn-submit">
                            <a href="php/view/cadastroTalento.php" style="background: #007bff; color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Cadastrar-Se</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

</body>

</html>