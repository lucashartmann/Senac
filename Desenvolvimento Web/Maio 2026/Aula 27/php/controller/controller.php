<?php


include_once '../model/talentoDAO.php';
include_once '../model/talento.php';
include_once '../model/validacao.php';
include_once '../model/seguranca.php';
include_once '../database/conexaoBanco.php';
include_once '../model/usuario.php';


// ob_start();
// header('Content-Type: application/json');
ini_set('display_errors', 0);
error_reporting(E_ALL);
$acao = $_GET['acao'] ?? NULL;

switch ($acao) {
    case "logar":
        realizarLogin();
        break;
    case "deslogar":
        deslogar();
        break;
    case "cadastrar":
        cadastrarTalento();
        break;
    case "excluir":
        excluirTalento();
        break;
    case "atualizar":
        atualizarTalento();
        break;
    default:
        header("Location: ../view/erro.php?mensagem=Ação inválida.");
        exit;
}

function atualizarTalento()
{
    session_start();
    Segurança::verificarAcesso();
    $id = isset($_POST['id']) ? intval($_POST['id']) : 0;
    $nome = isset($_POST['nome']) ? trim($_POST['nome']) : '';
    $email = isset($_POST['email']) ? trim($_POST['email']) : '';
    $telefone = isset($_POST['fone']) ? trim($_POST['fone']) : '';
    $tecnologia = isset($_POST['tecnologia']) ? trim($_POST['tecnologia']) : '';

    if ( empty($id) || empty($nome) || empty($tecnologia)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Os campos de Nome e Tecnologia são obrigatórios.</p>";
        header("Location: ../view/edicao.php?id=$id");
        exit;
    }

    if (!Validacao::validarEmail($email)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>E-mail inválido.</p>";
        header("Location: ../view/edicao.php?id=$id");
        exit;
    }

    if (!Validacao::validarTelefone($telefone)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Telefone inválido. Use o formato (XX) XXXXX-XXXX.</p>";
        header("Location: ../view/edicao.php?id=$id");
        exit;
    }

    if (!Validacao::validarNome($nome)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Nome inválido. Use apenas letras e espaços.</p>";
        header("Location: ../view/edicao.php?id=$id");
        exit;
    }

    if (!Validacao::validarTecnologias($tecnologia)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Tecnologia inválida. Use apenas letras, números e espaços.</p>";
        header("Location: ../view/edicao.php?id=$id");
        exit;
    }

    
    if ($id <= 0) {
        $_SESSION['mensagem'] = "<p class='error-msg'>ID de talento inválido.</p>";
        header("Location: ../view/edicao.php?id=$id");
        exit;
    }

    $talentoDAO = new TalentoDAO();
   
    $talento = new Talento();
    $talento->setId($id);
    $talento->setNome($nome);
    $talento->setEmail($email);
    $talento->setFone($telefone);
    $talento->setTecnologia($tecnologia);

    if ($talentoDAO->atualizar($talento)) {
        $_SESSION['mensagem'] = "<p class='success-msg'>Talento atualizado com sucesso!</p>";
        header("Location: ../view/consultaTalentos.php");
        exit;
    } else {
        $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao atualizar talento.</p>";
        header("Location: ../view/edicao.php?id=$id");
        exit;
    }
}

function excluirTalento()
{
    session_start();
    Segurança::verificarAcesso();
    $id = isset($_GET['id']) ? intval($_GET['id']) : 0;
    if ($id <= 0) {
        $_SESSION['mensagem'] = "<p class='error-msg'>ID de talento inválido.</p>";
        header("Location: ../view/consultaTalentos.php");
        exit;
    }

    $talentoDAO = new TalentoDAO();
    if ($talentoDAO->excluir($id)) {
        $_SESSION['mensagem'] = "<p class='success-msg'>Talento excluído com sucesso!</p>";
        header("Location: ../view/consultaTalentos.php");
        exit;
    } else {
        $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao excluir talento.</p>";
        header("Location: ../view/consultaTalentos.php");
        exit;
    }
}

function cadastrarTalento()
{
    session_start();
    Segurança::verificarAcesso();
    $nome = isset($_POST['nome']) ? trim($_POST['nome']) : '';
    $email = isset($_POST['email']) ? trim($_POST['email']) : '';
    $telefone = isset($_POST['telefone']) ? trim($_POST['telefone']) : '';
    $tecnologia = isset($_POST['tecnologia']) ? trim($_POST['tecnologia']) : '';

    if (empty($nome) || empty($tecnologia)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Os campos de Nome e Tecnologia são obrigatórios.</p>";
        header("Location: ../view/cadastro.php");
        exit;
    }

    if (!Validacao::validarEmail($email)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>E-mail inválido.</p>";
        header("Location: ../view/cadastro.php");
        exit;
    }

    if (!Validacao::validarTelefone($telefone)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Telefone inválido. Use o formato (XX) XXXXX-XXXX.</p>";
        header("Location: ../view/cadastro.php");
        exit;
    }

    $talento = new Talento();
    $talento->setNome($nome);
    $talento->setEmail($email);
    $talento->setFone($telefone);
    $talento->setTecnologia($tecnologia);

    $talentoDAO = new TalentoDAO();
    if ($talentoDAO->cadastrar($talento)) {
        $_SESSION['mensagem'] = "<p class='success-msg'>Talento cadastrado com sucesso!</p>";
        header("Location: ../view/consultaTalentos.php");
        exit;
    } else {
        $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao cadastrar talento.</p>";
        header("Location: ../view/cadastro.php");
        exit;
    }
}


function realizarLogin()
{
    session_start();
    $login = isset($_POST['usuario']) ? ($_POST['usuario'] ?? '') : '';
    $senha = isset($_POST['senha']) ? ($_POST['senha'] ?? '') : '';

    $conexao = ConexaoBanco::getInstancia();
    $sql = $conexao->prepare("SELECT * FROM usuarios WHERE login = ? AND senha = ?");
    $sql->execute(
        [$login, $senha]
    );
    $dados = $sql->fetch();
    if ($dados) {
        $usuario = new Usuario();
        $usuario->setLogin($dados['login']);
        $usuario->setPerfil($dados['perfil']);
        $_SESSION['usuario_logado'] = serialize($usuario);
        if ($usuario->getPerfil() == 'admin') {
            header("Location:../view/dashboard.php");
            exit;
        } else {
            header("Location:../view/resposta.php");
            exit;
        }
    } else {
        $sql = $conexao->prepare("SELECT * FROM talentos WHERE email = ? AND senha = ?");
        $sql->execute(
            [$login, $senha]
        );
        $dados = $sql->fetch();
        if ($dados) {
            $talento = new Talento();
            $talento->setId($dados['idTalento'] ?? 0);
            $talento->setNome($dados['nome'] ?? '');
            $talento->setEmail($dados['email'] ?? '');
            $talento->setFone($dados['fone'] ?? '');
            $talento->setTecnologia($dados['tecnologia'] ?? '');
            $talento->setSenha($dados['senha'] ?? '');
            $talento->setCurriculo($dados['curriculo'] ?? '');
            $_SESSION['usuario_logado'] = serialize($talento);
            header("Location:../view/resposta.php");
            exit;
        }
        else{
            header("Location:../../index.php?erro=1");
            exit;
        }
    }
}


function deslogar()
{
    session_start();
    Segurança::verificarAcesso();
    $_SESSION = array();

    if (ini_get("session.use_cookies")) {
        try {
            $params = session_get_cookie_params();
            setcookie(session_name(), "", time() - 42000, $params["path"], $params["domain"], $params['httponly']);
        } catch (Exception $e) {
            return;
        }
    }


    session_destroy();

    header("Location: ../../index.php");

    exit();
}
