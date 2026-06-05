<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/usuario.php";
include_once '../model/talento.php';

Segurança::verificarAcesso();

$aluno = unserialize($_SESSION['usuario_logado']);

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
    <title> Dashboard Talentos</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #12161a;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .dashboard-container {
            background-color: #1c2229;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
            width: 100%;
            max-width: 600px;
            box-sizing: border-box;
        }

        .header-dashboard {
            border-bottom: 1px solid #2c3540;
            padding-bottom: 20px;
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .header-dashboard h1 {
            margin: 0;
            font-size: 24px;
        }

        .btn-logout {
            background-color: #dc3545;
            color: #ffffff;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 14px;
            transition: background-color 0.3s;
        }

        .btn-logout:hover {
            background-color: #bd2130;
        }

        .welcome-box {
            background-color: #0f1316;
            padding: 20px;
            border-radius: 6px;
            border-left: 4px solid #28a745;
            margin-bottom: 30px;
        }

        .welcome-box p {
            margin: 5px 0;
            font-size: 16px;
        }

        .upload-section {
            background-color: #1a2026;
            border: 2px dashed #2c3540;
            padding: 30px;
            border-radius: 6px;
            text-align: center;
        }

        .file-input-wrapper {
            margin: 20px 0;
        }

        .btn-upload {
            background-color: #28a745;
            color: #ffffff;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .btn-upload:hover {
            background-color: #218838;
        }

        .cv-status {
            margin-top: 15px;
            font-size: 15px;
        }

        .link-cv {
            color: #38ef7d;
            text-decoration: none;
            font-weight: bold;
            border-bottom: 1px dashed #38ef7d;
        }

        .link-cv:hover {
            color: #11998e;
        }

        .error-msg { color: #ff4d4d; font-weight: bold; margin-top: 15px; text-align: center; }
        .success-msg { color: #2da44e; font-weight: bold; margin-top: 15px; text-align: center; }
    </style>
</head>
<body>

    <div class="dashboard-container">
        
        <div class="header-dashboard">
            <h1>Painel do Talento</h1>
            <a href="../controller/controller.php?acao=deslogar" class="btn-logout">Sair</a>
        </div>

        <div class="welcome-box">
            <p><strong>Bem-vindo(a),</strong> <?php echo htmlspecialchars($aluno->getNome() ?? 'Aluno'); ?>!</p>
            <p><strong>E-mail de Acesso:</strong> <?php echo htmlspecialchars($aluno->getEmail()); ?></p>
            <p><strong>Tecnologia Cadastrada:</strong> <?php echo htmlspecialchars($aluno->getTecnologia() ?? 'Não informada'); ?></p>
        </div>

        <?php if (isset($mensagem)) {
                echo $mensagem;
            } ?>

        <div class="upload-section">
            <h3>Enviar Currículo Profissional</h3>
            
            <form action="../controller/controller.php?acao=enviarCurriculo" method="POST" enctype="multipart/form-data">
                
                <div class="file-input-wrapper">
                    <input type="file" name="curriculo" accept=".pdf" required>
                </div>

                <button type="submit" class="btn-upload">Fazer Upload (.pdf)</button>
            </form>

            <div class="cv-status">
                <?php
                // Se no objeto o campo currículo não estiver nulo, exibe o link para o PDF
                if (!empty($aluno->getCurriculo())) {
                    echo "<p>🟢 <b>Status:</b> Currículo registrado!</p>";
                    echo "<p>📂 <a class='link-cv' href='../uploads/" . htmlspecialchars($aluno->getCurriculo()) . "' target='_blank'>Visualizar PDF Atual</a></p>";
                    echo "<form action='../controller/controller.php?acao=excluirCurriculo' method='POST' enctype='multipart/form-data'> <button type='submit' class='btn-logout'>Excluir Arquivo</button></form>";
                } else {
                    echo "<p>🔴 <b>Status:</b> Nenhum currículo em PDF enviado ainda.</p>";
                }
                ?>
            </div>
        </div>

    </div>

</body>
</html>