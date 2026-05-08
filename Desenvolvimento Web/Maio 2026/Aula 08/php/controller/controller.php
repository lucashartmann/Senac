<? 


require_once('../model/validacao.php');
require_once('../model/candidato.php');

if ($_SERVER["REQUEST_METHOD"] != "POST") {
    return;
}

$erros = [];

$nome = isset($_POST['nome']) ? trim(strtolower($_POST['nome'])) : "";
$idade = isset($_POST['idade']) ? (int)$_POST['idade'] : 0;
$email = isset($_POST['email']) ? trim(strtolower($_POST['email'])) : "";
$tech = isset($_POST['tech']) ? trim(strtolower($_POST['tech'])) : "";

if (!Validacao::validarNome($nome)) $erros[] = "Nome inválido!";
if (!Validacao::validarIdade($idade)) $erros[] = "Idade inválida!";
if (!Validacao::validarEmail($email)) $erros[] = "Email inválido!";
if (!Validacao::validarTech($tech)) $erros[] = "Tech inválida!";
if (!Validacao::converterTech($tech)) $erros[] = "Tech não pode ser convertido para lista!"; $tech = "";

$candidato1 = new Candidato($nome, $idade, $email);
$candidato1->setTech($tech);

if(empty($erros)){
    header(`Location: ../view/resposta.php?${$candidato1}`);
}

