<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/erro.css">
</head>

<body>
    <div id="wrapper">
        <header>
            <h1 style="color: #ff7b72;">Ops! Algo deu errado</h1>
        </header>
        <div class="container">
            <div class="post" style="border-color: #ff7b72;">
                <h2 class="title">Erro de processamento</h2>
                <div class="entry" style="text-align: center;">
                    <p>Infelizmente, ocorreu um erro durante a execução do sistema. Por favor, tente novamente mais tarde ou entre em contato com o suporte técnico.</p>
                    <div class="error-msg">
                        <?php
                        if (isset($_GET['mensagem'])) {
                            $mensagem = urldecode($_GET['mensagem']);
                            echo "<p><strong>Detalhes do erro:</strong> $mensagem</p>";
                        }
                        ?>
                    </div>
                    <hr style="border:0; border-top: 1px solid #30363d; margin: 20px 0;">
                    <a href="../../index.php" class="btn" style="color: #56a6ff; text-decoration: none;">&larr; Voltar para a página de login</a>
                </div>
            </div>
        </div>
        <footer><p>&copy; 2023 Lucas Augusto. Todos os direitos reservados.</p></footer>
    </div>
</body>

</html>