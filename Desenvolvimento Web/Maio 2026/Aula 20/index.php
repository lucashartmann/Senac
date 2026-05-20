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
                    <form action="php/controller/controller.php?acao=logar" method="POST">
                        <input type="username" name="usuario" placeholder="Digite o nome de usuário"  required>
                        <input type="password" name="senha" placeholder="Digite a senha de acesso" required >
                        <input type="submit" value="Entrar">
                        <?php
                            if(isset($_GET['erro'])) echo "<h3>ERRO</h3><p>Dados Inválidos</p>";
                        ?>
                    </form>
                </div>
            </div>
        </div>
    </div>

</body>

</html>