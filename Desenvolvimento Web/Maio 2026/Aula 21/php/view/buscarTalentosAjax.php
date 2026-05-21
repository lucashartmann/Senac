<?php
session_start();
include_once "../model/seguranca.php";
include_once "../model/talentoDAO.php";

Segurança::verificarAcesso();

$filtro = trim($_GET["pesquisa"]);
$talentoDAO = new TalentoDAO();

$talentos = [];

if (!empty($filtro)) {
    $talentos = $talentoDAO->buscarPorFiltro($filtro);
} else {
    $talentos = $talentoDAO->listarTodos();
}

if (empty($talentos)) {
    echo "<tr><td colspan='4'>Nenhum registro encontrado!</td></tr>";
} else {

    foreach ($talentos as $talento) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($talento['nome']) . "</td>";
        echo "<td>" . htmlspecialchars($talento['email']) . "</td>";
        echo "<td>" . htmlspecialchars($talento['fone']) . "</td>";
        echo "<td> <span>"
            . htmlspecialchars($talento['tecnologia'])
            . "</span></td>";
        echo "</tr>";
    }
}
