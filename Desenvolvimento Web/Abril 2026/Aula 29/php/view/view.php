<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de view</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<h1>
Dados Informados:</h1>
    <?php
    echo '<p>nome: ' . ($_GET['nome'] ?? '') . '<br>sexo: ' . ($_GET['sexo'] ?? '') . '<br>idade: ' . ($_GET['idade'] ?? '') . '</p>';
    ?>


</body>
</html>
