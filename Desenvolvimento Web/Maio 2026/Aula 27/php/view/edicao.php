<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/usuario.php";
include_once "../model/talentoDAO.php";

Segurança::verificarAcesso();

$usuario  = unserialize($_SESSION['usuario_logado']);
$id = isset($_GET['id']) ? intval($_GET['id']) : null;

if (!$id) {
    header("location: consultaTalentos.php");
}

$talentoDAO = new TalentoDAO();
$talentos = [];
$talento = $talentoDAO->buscarPorId($id);

if (!$talento) {
    $_SESSION['msg'] = "<p class='error-msg'>Talento não encontrado!</p>";
}

$mensagem = null;

if (isset($_SESSION['mensagem'])) {
    $mensagem = $_SESSION['mensagem'];
    unset($_SESSION['mensagem']);
}

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="../../css/base.css">
</head>

<body>
    <div id="wrapper">
        <header>
            <h2 style="text-align: center; margin-bottom:5px; color: #f0f6fc">
                Módulo de edição
            </h2>
            <p style="font-size: 0.9rem; color: #8b949e; margin-bottom: 0px;">Operador atual: <strong><?php echo $usuario->getLogin(); ?></strong>
                Nível: <?php echo $usuario->getPerfil() ?></p>
        </header>
        <hr>
        <div class="container">
            <div class="post">
                <h2 class="title">Alterar dados do currículo</h2>
                <nav class="menu-interno">
                    <a href="dashboard.php" style="color: #56a6ff; text-decoration:none;">&larr; Voltar ao Dashboard</a>
                    <a href="../controller/logout.php" style="color: #ff7b72; text-decoration:none;">&larr; Sair</a>
                </nav>
                <?php if (isset($mensagem)) {
                    echo $mensagem;
                } ?>
                <form action="../controller/controller.php?acao=atualizar" method="POST">
                    <input type="hidden" name="id" value="<?= $talento['idTalento'] ?>">
                    <div class="form-group">
                        <label for="nome">Nome:</label>
                        <input type="text" name="nome" id="nome" value="<?= htmlspecialchars($talento['nome']) ?>" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email:</label>
                        <input type="email" name="email" id="email" value="<?= htmlspecialchars($talento['email']) ?>" required>
                    </div>
                    <div class="form-group">
                        <label for="fone">Telefone:</label>
                        <input type="text" name="fone" id="fone" value="<?= htmlspecialchars($talento['fone']) ?>" required>
                    </div>
                    <div class="form-group">
                        <label for="tecnologia">Tecnologias:</label>
                        <input type="text" name="tecnologia" id="tecnologia" value="<?= htmlspecialchars($talento['tecnologia']) ?>" required>
                    </div>
                    <div class="form-actions btn-group">
                        <input type="submit" value="Atualizar Talento" class="btn-submit">
                        <input type="reset" value="Limpar" class="btn-reset">
                    </div>
                </form>
            </div>
        </div>
        <!-- <hr style="border:0; border-top: 1px solid #30363d; margin:30px; width: 100%;"> -->
        <footer style="text-align: center;">
            <p>&copy; 2026 Lucas Augusto. Todos os direitos reservados.</p>
        </footer>
    </div>
</body>



</html>