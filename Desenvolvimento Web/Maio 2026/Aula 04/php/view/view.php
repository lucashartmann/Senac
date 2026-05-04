<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../../css/view.css">
</head>
<body>
    <div class="container">
        <div class="box">
            <?php
            $validacao = $_GET['validacao'];
            $mensagem = $_GET['mensagem'] ?? '';
            echo "<h3>$mensagem</h3>";
            echo "<h4>$validacao</h4>";
            // echo "<h3>$validacao</h3>";
            // echo "<h4>Dados do Usuário: </h4>";
            // echo "<p>Email: $email</p>";
            // echo "<p>Senha: $senha</p>";
            ?>
            <a href="../../index.html">Voltar</a>
        </div>
</div>
</body>
</html>


