<?php

include '../model/pessoa.php';

$nome = $_POST['txtnome'] ;
$sexo = $_POST['txtsexo'] ;
$idade = $_POST['txtidade'] ;

$pessoa1 = new Pessoa($nome, $sexo);

$pessoa1->idade = $idade;

header("location: ../view/view.php?nome=$pessoa1->nome&sexo=$pessoa1->sexo&idade=$pessoa1->idade");

// echo $pessoa1;

// echo '<p>nome: ' . $pessoa1->nome . '<br>sexo: ' . $pessoa1->sexo . '<br>idade: ' . $pessoa1->idade . '</p>';