<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Erros</title>
    <link rel="stylesheet" href="../../css/erro.css">
</head>

<body>
    <div>
        <h1>Erro: Dados inválidos</h1>
        <p>Por favor, verifique os dados inseridos e tente novamente.</p>
        <?php
        $erros = isset($_GET['erros']) ? unserialize($_GET['erros']) : [];
        echo "<ul>";
        foreach ($erros as $erro) {
            echo "<li>" . htmlspecialchars($erro) . "</li>";
        }
        echo "</ul>";
        ?>
        <a href="../../index.php">Voltar</a>
    </div>
</body>

</html>