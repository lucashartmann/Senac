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
    if (isset($_GET['erros'])) {
        $erros = unserialize($_GET['erros']);
        echo "<h1>Erros encontrados:</h1><ul>";
        foreach ($erros as $erro) {
            echo "<li>" . htmlspecialchars($erro) . "</li>";
        }
        echo "</ul>";
    } else {
        echo "<p>Nenhum erro encontrado.</p>";
    }   
    ?>
    <a href="../../index.html">Voltar para o formulário</a>
</body>
</html>