<?php
session_start();

include_once '../model/usuario.php';
include_once "../model/seguranca.php";

Segurança::verificarAcesso();

$usuario = unserialize($_SESSION['usuario_logado']);

if (isset($_SESSION['mensagem'])) {
    $mensagem = $_SESSION['mensagem'];
    unset($_SESSION['mensagem']);
}


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
            <p style="font-size: 0.9rem; color: #8b949e; margin-bottom: 0px;">Operador atual: <strong><?php echo $usuario->getLogin(); ?></strong>
                Nível: <?php echo $usuario->getPerfil() ?></p>
        </header>
        <hr style="border:0; border-top: 1px solid #30363d; margin-bottom:30px; width: 100%;"">
        <div class=" container">
        <div class="post">
            <h2 class="title">Inserir novo talento</h2>
            <nav class="menu-interno">
                <a href="dashboard.php" style="color: #56a6ff; text-decoration:none;">&larr; Voltar ao Dashboard</a>
                <a href="../controller/controller.php?acao=deslogar" style="color: #ff7b72; text-decoration:none;">&larr; Sair</a>
            </nav>
            <?php if (isset($mensagem)) {
                echo $mensagem;
            } ?>
            <form action="../controller/controller.php?acao=cadastrar" method="post">
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
                    <input type="text" id="telefone" name="fone" placeholder="Ex: (11) 99999-9999" required>
                </div>
                <div class="form-group">
                    <label for="tecnologia">Tecnologia:</label>
                    <input type="text" id="tecnologia" name="tecnologia" placeholder="Ex: PHP, JavaScript, Python" required>
                </div>
                <div class="form-actions btn-group">
                    <input type="submit" value="Salvar Talento" class="btn-submit">
                    <input type="reset" value="Limpar" class="btn-reset">
                </div>
            </form>
        </div>
    </div>
    <!-- <hr style="border:0; border-top: 1px solid #30363d; margin: 20px 0;"> -->
    <footer style="text-align: center;">
        <p>&copy; 2026 Lucas Augusto. Todos os direitos reservados.</p>
    </footer>
    </div>
</body>

</html>