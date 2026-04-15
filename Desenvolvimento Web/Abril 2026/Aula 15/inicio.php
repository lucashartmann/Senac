<?php
    echo "<p>Teste de PHP</p>";

    $nome = "Lucas";
    echo "<p>Meu nome é $nome</p>";

    $valor = 10;
    $formato = "R$%.2f";
    printf($formato, $valor);

    $x = 2;
   
    echo "<br> $x + 2 = " . ($x + 2);

    echo "<br> 5 - $x = " . (5 - $x);

    echo "<br> 5 * $x = " . (5 * $x);

    echo "<br> 5 / $x = " . (5 / $x);

    echo "<br> 5 % $x = " . (5 % $x);

    echo "<br> ++$x = " . (++$x);

    echo "<br> --$x = " . (--$x);

    $x = 8;
    $y = 3;
    $x -= $y;
    echo "<br> $x -= $y = " . $x;

    $x = 10;
    $y = 2;
    $x *= $y;
    echo "<br> $x *= $y = " . $x;

    $x /= $y;
    echo "<br> $x /= $y = " . $x;

    $x = 10;
    $y = 3;
    $x %= $y;
    echo "<br> $x %= $y = " . $x;

    $texto = "Olá";
    $sufixo = " Mundo";
    $texto .= $sufixo;
    echo "<br> $texto";
?>