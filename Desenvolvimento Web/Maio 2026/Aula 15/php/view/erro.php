<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../../css/erro.css">
</head>
<body>
    <?php
    if (isset($_GET['mensagem'])) {
        $mensagem = urldecode($_GET['mensagem']);
        echo "<div class='erro-container'><h1>Ocorreu um erro</h1><p>$mensagem</p></div>";
    } else {
        echo "<div class='erro-container'><h1>Ocorreu um erro desconhecido</h1><p>Por favor, tente novamente mais tarde.</p></div>";
    }
    ?>
</body>
</html>