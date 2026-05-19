<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/talentoDAO.php";
include_once "../model/usuario.php";

Segurança::verificarAcesso();

$usuario = unserialize($_SESSION['usuario_logado']);
$talentoDAO = new TalentoDAO();
$talentos = $talentoDAO->listarTodos();
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta de Talentos</title>
    <link rel="stylesheet" href="../../css/base.css">
</head>

<body>
    <div id="wrapper">

        <!-- <header>
            <h2>
                Módulo de consulta
            </h2>
            <p>Operador atual: <strong><?php echo $usuario->getLogin(); ?></strong>
                Nível: <?php echo $usuario->getPerfil() ?></p>
        </header> -->

        <div class="container">
            <h2>Consulta de Talentos Cadastrados</h2>
            <?php if (empty($talentos)): ?>
                <p>Nenhum registro encontrado!</p>
            <?php else: ?>
                <table border="1" style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background-color: #21262d;">
                            <th>Nome</th>
                            <th>Email</th>
                            <th>Telefone</th>
                            <th>Tecnologias</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($talentos as $t): ?>
                            <tr>
                                <td><?php echo htmlspecialchars($t['nome']); ?></td>
                                <td><?php echo htmlspecialchars($t['email']); ?></td>
                                <td><?php echo htmlspecialchars($t['fone']); ?></td>
                                <td><?php echo htmlspecialchars($t['tecnologia']); ?></td>
                            </tr>
                        <?php endforeach ?>
                    </tbody>
                </table>
            <?php endif ?>
        </div>
        <footer>
            <a href="dashboard.php">&larr; Voltar ao Dashboard</a>
            <a href="cadastro.php">&larr; Cadastrar Talento</a>
            <a href="../controller/logout.php" style="color: #ff7b72; margin-left:20px;">&larr; Sair</a>
            <p>&copy; 2026 Lucas Augusto. Todos os direitos reservados.</p>
        </footer>
</body>

</html>