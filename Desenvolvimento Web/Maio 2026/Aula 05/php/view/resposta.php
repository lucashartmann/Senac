<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resposta</title>
    <link rel="stylesheet" href="../../css/resposta.css">
</head>
<body>
    <h1>Resposta</h1>
    <?php 
        $nome = $_GET['nome'];
        $email = $_GET['email'];
        $telefone = $_GET['telefone'];
        echo "<p>Nome: " . htmlspecialchars($nome) .  "</p>";
        echo "<p>Email: " . htmlspecialchars($email) . "</p>";
        echo "<p>Telefone: " . htmlspecialchars($telefone) . "</p>";
    ?>
</body>
</html>