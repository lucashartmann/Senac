<?php

require_once 'calculadora2.php';

$calculadora = new Calculadora(8, 2);

echo 'Soma: ' . $calculadora->getNum1() . " + " . $calculadora->getNum2() . " = " . $calculadora->somar() . '<br>';

echo 'Subtração: ' . $calculadora->getNum1() . " - " . $calculadora->getNum2() . " = " . $calculadora->diminuir() . '<br>';

echo 'Divisão: ' . $calculadora->getNum1() . " / " . $calculadora->getNum2() . " = " . $calculadora->dividir() . '<br>';

echo 'Multiplicação: ' . $calculadora->getNum1() . " * " . $calculadora->getNum2() . " = " . $calculadora->multiplicar();
