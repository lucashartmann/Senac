<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $email =  $_POST["email"];
    $assunto = $_POST["assunto"];
    $idade = $_POST["idade"];
    if (!in_array("newsletter", $_POST)) {
        $newsletter = 0;
    } else {
        $newsletter = $_POST["newsletter"];
    }

    echo  "Nome: $nome <br><br> Email: $email <br><br> Assunto: $assunto <br><br> Idade: $idade <br><br> Newsletter: $newsletter";

    echo "<br><br><a href='formulario.html'>Voltar</a>";
} else {
    echo "ERRO! Requisição inválida.";
}
?>
