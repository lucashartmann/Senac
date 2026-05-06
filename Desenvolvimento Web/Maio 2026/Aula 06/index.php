<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Pessoa</title>
    <link rel="stylesheet" href="css/index.css">
</head>

<body>
    <form action="php/controller/controller.php" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required>
        <label for="sobrenome">Sobrenome:</label>
        <input type="text" id="sobrenome" name="sobrenome" required>
        <label for="idade">Idade:</label>
        <input type="number" id="idade" name="idade" required>
        <input type="submit" value="Enviar">
    </form>
</body>

</html>