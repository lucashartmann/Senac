<?php
    if ($_SERVER['REQUEST_METHOD'] == "POST") {
        $preco = $_POST['preco'];
        $quantidade = $_POST['quantidade'];
        
        echo "<h3>Resultado do processamento do desconto</h3>";
        echo "<p> Preço unitário: " . number_format($preco, 2, ',', '.') . "</p>";
        echo "<p> Quantidade: $quantidade </p>";
        $desconto_desejado = $_POST['desconto'];
        echo "<p> Desconto desejado: $desconto_desejado%</p>";
        $total = $preco * $quantidade;
        echo "<p> Desconto sobre o valor total: " . ($total * ($desconto_desejado / 100)).  "</p>";
        $valor_total = $total - ($total * ($desconto_desejado / 100));

        echo "<p>Valor final: $valor_total</p>";
    } else {
        echo "<p>Acesso Inválido!! Por favor, preencha o formulário</p>";
    }
    echo "<p><a href='index.html'>Voltar</a></p>";
?>