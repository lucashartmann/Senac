http://tools.lymas.com.br/regexp_br.php


Exercício Prático: Sistema de Autenticação com Padrão MVC
Contexto
Você foi contratado para desenvolver o módulo de validação de uma nova plataforma educacional. Para garantir que o sistema seja seguro e de fácil manutenção, a equipe optou por utilizar o padrão MVC (Model-View-Controller) e a tipagem estrita do PHP 8.0.

Objetivo
Desenvolver um formulário de login que valide as credenciais do usuário (e-mail e senha) antes de processar o acesso, utilizando classes estáticas e expressões regulares.

Requisitos Técnicos
1. Camada Model (Validacao.class.php)
Crie uma classe chamada Validacao que utilize a diretiva strict_types. Esta classe deve conter:

Constantes: Duas constantes para armazenar as expressões regulares:

REGEX_EMAIL: Deve validar e-mails padrão (ex: nome@dominio.com).

REGEX_SENHA: Deve exigir no mínimo 6 caracteres, contendo ao menos uma letra e um número.

Método Estático: Um método chamado validar(string $expressao, string $valor): bool que retorne apenas verdadeiro ou falso.

2. Camada Controller (LoginController.php)
Este arquivo será o ponto de entrada. Ele deve:

Receber os dados via POST.

Invocar o Model para validar os campos.

Definir uma mensagem de sucesso ou erro.

Chamar a View para exibir o resultado ao usuário.

3. Camada View (login_view.php)
Crie uma interface simples em HTML/CSS contendo:

Um formulário com campos de e-mail e senha.

Um local para exibir as mensagens de feedback (utilize cores diferentes para erro e sucesso).