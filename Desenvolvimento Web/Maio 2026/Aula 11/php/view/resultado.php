<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../../css/resultado.css">
</head>
<body>
    <div>
    <?php 
    if (isset($_GET['candidato'])) {
        $candidato = $_GET['candidato'];
        echo $candidato;
    } else {
        echo "<p>Nenhum candidato encontrado.</p>";
    }
    ?>
    </div>
</body>
</html>