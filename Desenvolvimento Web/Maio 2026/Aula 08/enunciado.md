1. Exercício Prático: Sistema de Triagem "Tech Talent"Objetivo: Criar um arquivo chamado processa_candidato.php que receba dados de um formulário (ou simulados via array) e aplique as funções nativas do PHP para higienização e validação.1
. O CenárioVocê recebeu uma lista de dados de um candidato que se inscreveu para uma vaga de desenvolvedor. Os dados estão "sujos" (com espaços extras e letras despadronizadas).


2. Requisitos do ScriptCrie um código que realize as seguintes etapas:Higienização de Strings:Remova espaços desnecessários do início e fim do nome e e-mail.  Converta o e-mail para letras minúsculas.  Formate o nome para que cada primeira letra seja maiúscula (ex: "claudio alves" -> "Claudio Alves").  Validações Críticas:Verifique se a idade informada é um número e se está entre 18 e 100 anos.  Valide se o e-mail possui um formato válido.  Utilize o operador de coalescência nula (??) para garantir que o script não quebre caso algum campo falte.  Manipulação de Arrays:O candidato enviou as tecnologias que domina em uma única string separada por vírgulas (ex: "PHP, Rust, JavaScript"). Converta essa string em um Array.  Ordene esse array de tecnologias em ordem alfabética.  Conte quantas tecnologias ele domina.  

3. Modelo de Partida (Código para os alunos completarem)PHP<?php
// Configuração inicial
date_default_timezone_set('America/Sao_Paulo'); // [cite: 229]

// Dados Simulados (podem vir do $_POST)
$nomeBruto = "  roberto silva  ";
$emailBruto = "CONTATO@Email.Com  ";
$idadeBruta = "25";
$techsBrutas = "PHP, JavaScript, Rust, Python, Docker";

// --- INÍCIO DO EXERCÍCIO ---

// 1. Higienize o nome e o e-mail
$nome = ""; // Use trim e ucwords
$email = ""; // Use trim e strtolower

// 2. Valide a idade (deve ser numérica e entre 18 e 100)
$idade = $idadeBruta ?? 0;
$idadeValida = false; // Crie a lógica com if e is_numeric

// 3. Valide o e-mail
$emailValido = false; // Use filter_var

// 4. Transforme a string de tecnologias em um Array e ordene
$arrayTechs = []; // Use explode
// Aplique a ordenação aqui

// --- SAÍDA DE DADOS (Relatório) ---
echo "<h3>Relatório do Candidato</h3>";
echo "Nome Formatado: $nome <br>";
echo "E-mail: " . ($emailValido ? $email : "INVÁLIDO") . "<br>";
echo "Idade: " . ($idadeValida ? "$idade anos" : "Idade fora do padrão") . "<br>";
echo "Total de Tecnologias: " . count($arrayTechs) . "<br>";
echo "Lista de Techs: " . implode(" | ", $arrayTechs); // [cite: 354]
?>