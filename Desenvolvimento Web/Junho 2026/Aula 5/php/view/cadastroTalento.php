<?php
session_start();
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
        <div class=" container" style="width: 620px; margin: 0 0; padding: 20px; background: #1e222b; color: #fff; border-radius: 8px;">
            <div class="post" style="width: 580px; max-width: 3000px; margin: 0 auto;">
                <h2 class="title">Cadastro</h2>
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
                    <div class="form-group">
                        <label for="senha">Senha:</label>
                        <input type="password" id="senha" name="senha" placeholder="Ex: ********" required>
                    </div>
                    <div class="form-actions btn-group">
                        <input type="submit" value="Cadastrar" class="btn-submit">
                        <input type="reset" value="Limpar" class="btn-reset">
                        <a href="../../index.php" style="background: #007bff; color: #fff; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Voltar</a>
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