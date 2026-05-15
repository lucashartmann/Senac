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
    include_once '../model/candidato.php';
    session_start();
    if (isset($_SESSION['candidato'])) {
        $candidato = unserialize($_SESSION['candidato']);
        echo $candidato;
    } else {
        echo "<p>Nenhum candidato encontrado.</p>";
    }
    ?>
    </div>
</body>
</html>
