<?php


include_once '../model/validacao.php';
include_once '../model/candidato.php';

date_default_timezone_set('America/Sao_Paulo');

if ($_SERVER["REQUEST_METHOD"] != "POST") {
    header("Location: ../../index.html");
    exit();
}

$nome = isset($_POST['nome']) ? trim(strtolower($_POST['nome'])) : "";
$idade = isset($_POST['idade']) ? (int)$_POST['idade'] : 0;
$email = isset($_POST['email']) ? trim(strtolower($_POST['email'])) : "";
$tech = isset($_POST['tech']) ? trim(strtolower($_POST['tech'])) : "";

if (!Validacao::validarNome(($nome))) $nome = NULL ;
if (!Validacao::validarIdade(($idade))) $idade = NULL ;
if (!Validacao::validarEmail(($email))) $email = NULL ;
if (!Validacao::validarTech(($tech))) $tech = [] ;
else $tech = Validacao::converterTech(($tech));

$candidato = new Candidato($nome, $email, $idade);
$candidato->setTech($tech);

header("Location: ../view/resultado.php?candidato=" . urlencode($candidato));
