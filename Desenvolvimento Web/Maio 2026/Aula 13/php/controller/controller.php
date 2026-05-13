<?php


include_once '../model/validacao.php';
include_once '../model/candidato.php';


session_start();

if ($_SERVER["REQUEST_METHOD"] != "POST") {
    header("Location: ../../index.html");
    exit();
}

$nome = isset($_POST['nome']) ? trim(strtolower($_POST['nome'])) : "";
$idade = isset($_POST['idade']) ? (int)$_POST['idade'] : 0;
$email = isset($_POST['email']) ? trim(strtolower($_POST['email'])) : "";
$tech = isset($_POST['tech']) ? trim(   strtolower($_POST['tech'])) : "";

if (!Validacao::validarNome(($nome))) $nome = NULL ;
if (!Validacao::validarIdade(($idade))) $idade = NULL ;
if (!Validacao::validarEmail(($email))) $email = NULL ;
if (!Validacao::validarTech(($tech))) $tech = [] ;
else $tech = Validacao::converterTech(($tech));

$candidato = new Candidato($nome, $email, $idade);
$candidato->setTech($tech);
$candidato->calcularPontos();
$candidato->definirClassificacao();

print_r($tech);

// $_SESSION['candidato'] = [
//     "Nome" => $candidato->getNome(),
//     "Email" => $candidato->getEmail(),
//     "Idade" => $candidato->getIdade(),
//     "Techs" => $candidato->getTech()
// ];

// <?php 
//     session_start();
//     if (isset($_SESSION['candidato'])) {
//         $candidato = $_SESSION['candidato'];
//         echo "<h1>Resultado do Cadastro</h1>";
//         echo "<p><strong>Nome:</strong> " . htmlspecialchars($candidato['Nome']) . "</p>";
//         echo "<p><strong>Email:</strong> " . htmlspecialchars($candidato['Email']) . "</p>";
//         echo "<p><strong>Idade:</strong> " . htmlspecialchars($candidato['Idade']) . "</p>";
//         echo "<p><strong>Techs:</strong> " . htmlspecialchars(implode(", ", $candidato['Techs'])) . "</p>";
//     } else {
//         echo "<p>Nenhum candidato encontrado.</p>";
//     }

$_SESSION['candidato'] = serialize($candidato);

header("Location: ../view/resultado.php?");
