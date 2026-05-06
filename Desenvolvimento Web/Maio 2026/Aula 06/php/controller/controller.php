<?php

include_once '../model/pessoa.php';
include_once '../model/validacao.php';

$erros = array();

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ../../index.php');
    exit();
}

$nome = isset($_POST['nome']) ? trim(strtolower($_POST['nome'])) : '';
$sobrenome = isset($_POST['sobrenome']) ? trim(strtolower($_POST['sobrenome'])) : '';
$idade = isset($_POST['idade']) ? (int)$_POST['idade'] : 0;

if (!Validacao::validarNome(($nome))) $erros[] = "Nome inválido";

if (!Validacao::validarNome(($sobrenome))) $erros[] = "Sobrenome inválido";

if (!Validacao::validarIdade($idade)) $erros[] = "Idade inválida";


if (empty($erros)) {
    $pessoa = new Pessoa($nome, $sobrenome, $idade);
    header('Location: ../view/resposta.php?pessoa=' . $pessoa);
    exit();
} else {
    header('Location: ../view/erro.php?erros=' . serialize($erros));
    exit();
}
