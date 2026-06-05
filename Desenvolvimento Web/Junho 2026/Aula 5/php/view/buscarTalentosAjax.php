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
        $nome = mb_convert_encoding($talento->getNome(), 'UTF-8', 'auto');
        $tecnologia = mb_convert_encoding($talento->getTecnologia(), 'UTF-8', 'auto');
        echo "<tr>";
        echo "<td>" . htmlspecialchars($nome) . "</td>";
        echo "<td>" . htmlspecialchars($talento->getEmail()) . "</td>";
        echo "<td>" . htmlspecialchars($talento->getFone()) . "</td>";
        echo "<td> <span>"
            . htmlspecialchars($tecnologia)
            . "</span></td>";
        echo "<td>  
            <a href='edicao.php?id=" . $talento->getId() . "' class=\"btn-acao btn-editar\">Editar</a>
            <a href=\"../controller/controller.php?acao=excluir&id=" . $talento->getId() . "\" class=\"btn-acao btn-excluir\" onclick=\"return confirm('Tem certeza que deseja excluir este talento?')\">Excluir</a>
            </td>";
        echo "</tr>";
    }
}
