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
session_start();
$acao = $_GET['acao'] ?? 'logar';

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
    default:
        header("Location: ../view/erro.php?mensagem=Ação inválida.");
        exit;
}

function cadastrarTalento()
{
    
    Segurança::verificarAcesso();
    $nome = isset($_POST['nome']) ? trim($_POST['nome']) : '';
    $email = isset($_POST['email']) ? trim($_POST['email']) : '';
    $telefone = isset($_POST['telefone']) ? trim($_POST['telefone']) : '';
    $tecnologia = isset($_POST['tecnologia']) ? trim($_POST['tecnologia']) : '';

    if(empty($nome) || empty($tecnologia)) {
        header("Location: ../view/erro.php?mensagem=Os campos de Nome e Tecnologia são obrigatórios.");
        exit;
    }

    if (!Validacao::validarEmail($email)) {
        header("Location: ../view/erro.php?mensagem=E-mail inválido.");
        exit;
    }

    if (!Validacao::validarTelefone($telefone)) {
        header("Location: ../view/erro.php?mensagem=Telefone inválido. Use o formato (XX) XXXXX-XXXX.");
        exit;
    }

    $talento = new Talento();
    $talento->setNome($nome);
    $talento->setEmail($email);
    $talento->setFone($telefone);
    $talento->setTecnologia($tecnologia);

    $talentoDAO = new TalentoDAO();
    if ($talentoDAO->cadastrar($talento)) {
        header("Location: ../view/consultaTalentos.php?mensagem=Talento cadastrado com sucesso!");
        exit;
    } else {
        header("Location: ../view/erro.php?mensagem=Erro ao cadastrar talento.");
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
        } else {
            header("Location:../view/resposta.php");
        }
    } else {
        header("Location:../../index.php?erro=1");
    }
}

function deslogar()
{
    
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
