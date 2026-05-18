<?php
session_start();

include_once '../model/usuario.php';
include_once "../model/seguranca.php";

Segurança::verificarAcesso();

$usuario = unserialize($_SESSION['usuario_logado']);


?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Talento</title>
    <link rel="stylesheet" href="../../css/base.css">
</head>

<body>
    <div id="wrapper">
        <header>
            <h2>
                Módulo de cadastro
            </h2>
            <p>Operador atual: <strong><?php echo $usuario->getLogin(); ?></strong>
                Nível: <?php echo $usuario->getPerfil() ?></p>
        </header>
        <hr style="border:0; border-top: 1px solid #30363d; margin: 20px 0;">
        <div class="container">
            <div class="post">
                <h2 class="title">Inserir novo talento</h2>
                <form action="../controller/controller.php" method="post">
                    <div class="form-group">
                        <label for="nome">Nome Completo:</label>
                        <input type="text" id="nome" name="nome" placeholder="Ex: João da Silva" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email do contato:</label>
                        <input type="email" id="email" name="email" placeholder="Ex: contato@exemplo.com" required>
                    </div>
                    <div class="form-group">
                        <label for="telefone">Telefone / Celular:</label>
                        <input type="text" id="telefone" name="telefone" placeholder="Ex: (11) 99999-9999" required>
                    </div>
                    <div class="form-group">
                        <label for="tecnologia">Tecnologia:</label>
                        <input type="text" id="tecnologia" name="tecnologia" placeholder="Ex: PHP, JavaScript, Python" required>
                    </div>
                    <div class="form-group btn-group">
                        <input type="submit" value="Salvar Talento" class="btn-submit">
                        <input type="reset" value="Limpar" class="btn-reset">
                    </div>
                </form>
            </div>
        </div>
        <hr style="border:0; border-top: 1px solid #30363d; margin: 20px 0;">
        <footer><a href="dashboard.php">&larr; Voltar ao Dashboard</a><a href="consulta.php">&larr; Ver Talentos</a><a href="../controller/logout.php" style="color: #ff7b72; margin-left:20px;">&larr; Sair</a>
            <p>&copy; 2023 Lucas Augusto. Todos os direitos reservados.</p>
        </footer>
    </div>
</body>

</html>