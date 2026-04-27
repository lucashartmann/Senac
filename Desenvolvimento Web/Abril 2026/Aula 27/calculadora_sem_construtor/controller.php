<?php

require_once 'calculadora.php';

$calculadora = new Calculadora();

$calculadora->setNum1(8);
$calculadora->setNum2(2);

echo 'Soma: ' . $calculadora->getNum1() . " + " . $calculadora->getNum2() . " = " . $calculadora->somar() . '<br>';

echo 'Subtração: ' . $calculadora->getNum1() . " - " . $calculadora->getNum2() . " = " . $calculadora->diminuir() . '<br>';

echo 'Divisão: ' . $calculadora->getNum1() . " / " . $calculadora->getNum2() . " = " . $calculadora->dividir() . '<br>';

echo 'Multiplicação: ' . $calculadora->getNum1() . " * " . $calculadora->getNum2() . " = " . $calculadora->multiplicar();
