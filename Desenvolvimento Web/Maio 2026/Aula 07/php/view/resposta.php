<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="../../css/resposta.css">
</head>

<body>
    <div>
    <h3>Pessoa Cadastrada!</h3>
    <?php $pessoa = $_GET['pessoa'] ?? null;
    echo $pessoa;
    ?>
    <a href="../../index.php">Voltar</a>
    </div>
</body>

</html>