<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/talentoDAO.php";
include_once "../model/usuario.php";
Segurança::verificarAcesso();
$usuario = unserialize($_SESSION['usuario_logado']);
$talentoDAO = new TalentoDAO();
$talentos = [];
$talentos = $talentoDAO->listarTodos();

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
    <title>Consulta de Talentos</title>
    <link rel="stylesheet" href="../../css/base.css">
</head>

<body>
    <div id="wrapper" class="dashboard-container">
        <div class="container">
            <header>
                <h2>
                    Módulo de consulta
                </h2>
                <p style="font-size: 0.9rem; color: #8b949e; margin-bottom: 0px;">Operador atual: <strong><?php echo $usuario->getLogin(); ?></strong>
                    Nível: <?php echo $usuario->getPerfil() ?></p>
            </header>
            <hr>
            <div class="post">
                <nav class="menu-interno">
                    <a href="dashboard.php" style="color: #56a6ff; text-decoration:none;">&larr; Voltar ao Dashboard</a>
                    <a href="../controller/logout.php" style="color: #ff7b72; text-decoration:none;">&larr; Sair</a>
                </nav>
                <div class="container">
                    <h2>Consulta de Talentos Cadastrados</h2>
                    <?php if (empty($talentos)): ?>
                        <p>Nenhum registro encontrado!</p>
                    <?php else: ?>
                        <form onsubmit="return false;" style="margin-bottom:25px;">
                            <input type="text" id="pesquisa" name="pesquisa" placeholder="Digite o filtro" style="width: 100%; margin-bottom:0; margin-top:30px;">
                        </form>
                        <table border="1" style="width: 100%; border-collapse: collapse;">
                            <thead>
                                <tr>
                                    <th>Nome</th>
                                    <th>Email</th>
                                    <th>Telefone</th>
                                    <th>Tecnologias</th>
                                    <th style="width: 160px; text-align: center;">Ações</th>
                                </tr>
                            </thead>
                            <tbody id="corpo-tabela">
                                <?php foreach ($talentos as $t): ?>
                                    <tr>
                                        <td><?php echo htmlspecialchars($t['nome']); ?></td>
                                        <td><?php echo htmlspecialchars($t['email']); ?></td>
                                        <td><?php echo htmlspecialchars($t['fone']); ?></td>
                                        <td>
                                            <span>
                                                <?php echo htmlspecialchars(mb_convert_encoding($t['tecnologia'], 'UTF-8', 'auto')); ?>
                                            </span>
                                        </td>
                                        <td style="text-align:center;">
                                            <a href="edicao.php?id=<?php echo $t['idTalento']; ?>" class="btn-acao btn-editar">Editar</a>
                                            <a href="../controller/controller.php?acao=excluir&id=<?php echo $t['idTalento']; ?>" class="btn-acao btn-excluir" onclick="return confirm('Tem certeza que deseja excluir este talento?')">Excluir</a>
                                        </td>
                                    </tr>
                                <?php endforeach ?>
                            </tbody>
                        </table>
                    <?php endif ?>
                </div>
            </div>
            <hr style="border:0; border-top: 1px solid #30363d; margin:30px; width: 100%;">
            <footer style="text-align: center;">
                <p>&copy; 2026 Lucas Augusto. Todos os direitos reservados.</p>
            </footer>
        </div>
    </div>

        <script>
            const input = document.getElementById('pesquisa');
            const corpoTabela = document.getElementById('corpo-tabela');
            input.addEventListener('input', function() {
                let termo = input.value;
                fetch('buscarTalentosAjax.php?pesquisa=' + encodeURIComponent(termo))
                    .then(response => response.text())
                    .then(html => {
                        corpoTabela.innerHTML = html;
                    })
                    .catch(erro => console.error('Erro na busca em tempo real:', erro));
            });
        </script>

</body>

</html>