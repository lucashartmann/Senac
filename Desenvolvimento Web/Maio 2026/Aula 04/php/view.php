<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../css/view.css">
</head>
<body>
    <?php
    $email = $_GET['email'];
    $senha = $_GET['senha'];
    $mensagem = $_GET['mensagem'] ?? '';
    echo "<h3>$mensagem</h3>";
    // echo "<h4>Dados do Usuário: </h4>";
    // echo "<p>Email: $email</p>";
    // echo "<p>Senha: $senha</p>";
    ?>
    <a href="../index.html">Voltar</a>
</body>
</html>


