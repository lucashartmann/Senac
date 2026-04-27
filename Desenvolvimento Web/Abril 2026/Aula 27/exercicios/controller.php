<?php

require_once 'produto.php';
require_once 'veiculo.php';
require_once 'aluno.php';

$produto1 = new Produto();

$produto1->setNome("Notebook");
$produto1->setValor(3500);

echo '<h3>Produto:</h3>' . '<p>Nome: ' . $produto1->getNome() . "</p><p>Valor: R$" . $produto1->getValor() . "</p>";  

$veiculo = new Veiculo("Toyota", "Corolla");

echo '<h3>Veiculo:</h3>';

echo $veiculo->exibirDados();

echo '<h3>Aluno:</h3>';

$aluno1 = new Aluno("Lucas");
$aluno1->setNota1(10.0);
$aluno1->setNota2(2.5);

echo 'O aluno ' . $aluno1->getNome() . " ficou com média " . $aluno1 -> calcularMedia();