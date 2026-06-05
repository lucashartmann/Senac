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
    case "enviarCurriculo":
        enviarCurriculo();
        break;
    case "excluirCurriculo":
        excluirCurriculo();
        break;
    default:
        header("Location: ../view/erro.php?mensagem=Ação inválida.");
        exit;
}

function excluirCurriculo()
{
    session_start();
    Segurança::verificarAcesso();
    if (!isset($_SESSION["usuario_logado"])) {
        header("Location: ../view/erro.php?mensagem=Usuário não autenticado.");
        exit;
    }
    $talento = unserialize($_SESSION['usuario_logado']);
    $talentoDAO = new TalentoDAO();

    if (!$talento || !($talento instanceof Talento)) {
        header("Location: ../view/erro.php?mensagem=Usuário inválido.");
        exit;
    }

    $curriculo = $talento->getCurriculo();

    if ($curriculo) {
        $nome = $curriculo;
        $diretorio = '../uploads/';
        if (!is_dir($diretorio)) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro diretório inexistente.</p>";
            header("Location: ../view/respostaTalento.php");
        }

        $caminho = $diretorio . $nome;

        if (unlink($caminho)) {
            if ($talentoDAO->atualizarCurriculo($talento->getId(), null)) {
                $talento->setCurriculo(null);
                $_SESSION['usuario_logado'] = serialize($talento);
                $_SESSION['mensagem'] = "<p class='success-msg'>Currículo removido com sucesso!</p>";
                header("Location: ../view/respostaTalento.php");
                exit;
            } else {
                $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao remover currículo no banco de dados.</p>";
                header("Location: ../view/respostaTalento.php");
                exit;
            }
        } else {
            $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao remover arquivo enviado.</p>";
            header("Location: ../view/respostaTalento.php");
            exit;
        }
    } else {
        $_SESSION['mensagem'] = "<p class='error-msg'>Não há nenhum curriculo cadastrado.</p>";
        header("Location: ../view/respostaTalento.php");
        exit;
    }
}

function enviarCurriculo()
{
    session_start();
    Segurança::verificarAcesso();
    if (!isset($_SESSION["usuario_logado"])) {
        header("Location: ../view/erro.php?mensagem=Usuário não autenticado.");
        exit;
    }
    $talento = unserialize($_SESSION['usuario_logado']);
    $talentoDAO = new TalentoDAO();

    if (!$talento || !($talento instanceof Talento)) {
        header("Location: ../view/erro.php?mensagem=Usuário inválido.");
        exit;
    }

    if (isset($_FILES['curriculo']) && $_FILES['curriculo']['error'] === UPLOAD_ERR_OK) {
        $arquivo = $_FILES['curriculo'];
        $extensao = strtolower(pathinfo($arquivo['name'], PATHINFO_EXTENSION));
        if ($extensao == 'pdf') {
            $novoNome = md5(uniqid(rand(), true)) . '.pdf';
            $diretorio = '../uploads/';
            if (!is_dir($diretorio)) {
                mkdir($diretorio, 0755, true);
            }

            if (move_uploaded_file($arquivo['tmp_name'], $diretorio . $novoNome)) {
                if ($talentoDAO->atualizarCurriculo($talento->getId(), $novoNome)) {
                    $talento->setCurriculo($novoNome);
                    $_SESSION['usuario_logado'] = serialize($talento);
                    $_SESSION['mensagem'] = "<p class='success-msg'>Currículo enviado com sucesso!</p>";
                    header("Location: ../view/respostaTalento.php");
                    exit;
                } else {
                    $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao atualizar currículo no banco de dados.</p>";
                    header("Location: ../view/respostaTalento.php");
                    exit;
                }
            } else {
                $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao mover o arquivo enviado.</p>";
                header("Location: ../view/respostaTalento.php");
                exit;
            }
        } else {
            $_SESSION['mensagem'] = "<p class='error-msg'>Formato de arquivo inválido. Apenas PDF é permitido.</p>";
            header("Location: ../view/respostaTalento.php");
            exit;
        }
    } else {
        $_SESSION['mensagem'] = "<p class='error-msg'>Nenhum arquivo enviado ou ocorreu um erro no upload.</p>";
        header("Location: ../view/respostaTalento.php");
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
    // Segurança::verificarAcesso();
    $location = "Location: ../view/cadastro.php";
    $id = isset($_POST['id']) ? intval($_POST['id']) : 0;
    $nome = isset($_POST['nome']) ? trim($_POST['nome']) : '';
    $email = isset($_POST['email']) ? trim($_POST['email']) : '';
    $telefone = isset($_POST['fone']) ?  trim($_POST['fone']) : '';
    $tecnologia = isset($_POST['tecnologia']) ? trim($_POST['tecnologia']) : '';
    $senha = isset($_POST['senha']) ? trim($_POST['senha']) : '';
    // $curriculo = isset($_FILES['curriculo']) ? $_FILES['curriculo'] : null;

    if (!isset($_SESSION['usuario_logado'])) {
        $location = "Location: ../view/cadastroTalento.php";
        if (empty($senha)) {
            $_SESSION['mensagem'] = "<p class='error-msg'>O campo de Senha é obrigatório para novos cadastros.</p>";
            header($location);
            exit;
        }
        if (!Validacao::validarSenha($senha)) {
            $_SESSION['mensagem'] = "<p class='error-msg'>Senha inválida. Use entre 6 e 20 caracteres.</p>";
            header($location);
            exit;
        }
    }

    if (empty($nome) || empty($tecnologia)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Os campos de Nome e Tecnologia são obrigatórios.</p>";
        header($location);
        exit;
    }

    if (!Validacao::validarEmail($email)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>E-mail inválido.</p>";
        header($location);
        exit;
    }

    if (!Validacao::validarTelefone($telefone)) {
        $_SESSION['mensagem'] = "<p class='error-msg'>Telefone inválido. Use o formato (XX) XXXXX-XXXX.</p>";
        header($location);
        exit;
    }

    $talento = new Talento();
    $talentoDAO = new TalentoDAO();
    $talento->setNome($nome);
    $talento->setEmail($email);
    $talento->setFone($telefone);
    $talento->setTecnologia($tecnologia);
    $talento->setSenha($senha);
    $talento->setCurriculo(null);

    if ($senha) {
        error_log("Senha recebida: " . $senha);
        $senhaHash = password_hash($senha, PASSWORD_DEFAULT);
        // $senhaHash = hash('sha256', $senha);
        $talento->setSenha($senhaHash);
    }

    if ($id > 0) {
        $talento->setId($id);
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


    if ($talentoDAO->cadastrar($talento)) {
        $_SESSION['mensagem'] = "<p class='success-msg'>Talento cadastrado com sucesso!</p>";
        if (!isset($_SESSION['usuario_logado'])) {
            $_SESSION['usuario_logado'] = serialize($talento);
            header("Location: ../view/respostaTalento.php");
            exit;
        }
        header("Location: ../view/consultaTalentos.php");
        exit;
    } else {
        $_SESSION['mensagem'] = "<p class='error-msg'>Erro ao cadastrar talento.</p>";
        header($location);
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
            $_SESSION['mensagem'] = 'Login realizado com sucesso!';
            header("Location:../view/dashboard.php");
            exit;
        } else {
            $_SESSION['mensagem'] = 'Login realizado com sucesso!';
            header("Location:../view/resposta.php");
            exit;
        }
    } else {
        $talentoDAO = new TalentoDAO();
        $talento = $talentoDAO->verificarLogin($login, $senha);
        if ($talento) {
            $_SESSION['usuario_logado'] = serialize($talento);
            $_SESSION['mensagem'] = 'Login realizado com sucesso!';
            header("Location:../view/respostaTalento.php");
            exit;
        } else {
            $_SESSION["mensagem"] = "Credenciais de talento inválidas. Tente novamente.";
            header("Location:../../index.php");
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
