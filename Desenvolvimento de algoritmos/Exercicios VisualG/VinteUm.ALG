Algoritmo "semnome"
// Disciplina   : Linguagem e L�gica de Programa��o
// Professor   : Miguel
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Lucas Augusto Hartmann
// Data atual  : 21/10/2024

Var
   nome, sobrenome, cidade, sexo, endereco : caractere
   idade : inteiro
   rg, cpf : caractere

Inicio
   Escreval("## CADASTRO LOJA MARCELINHO ##")
   Escreval("Informe o nome do cliente:")
   leia (nome)
   Escreval("Informe o sobrenome do cliente:")
   leia (sobrenome)
   Escreval("Informe a cidade do cliente:")
   leia (cidade)
   Escreval("Informe o sexo do cliente:")
   leia (sexo)
   Escreval("Informe o endere�o do cliente:")
   leia (endereco)
   Escreval("Informe a idade do cliente:")
   leia (idade)
   Escreval("Informe o RG do cliente:")
   leia (rg)
   Escreval("Informe o CPF do cliente:")
   leia (cpf)
   Escreval("#### Dados cadastrados! ####")
   Escreva("Nome: ", nome, " ", sobrenome, ", cidade: ", cidade)
   Escreva(", sexo: ", sexo, ", endere�o: ", endereco)
   Escreva(", idade: ", idade, ", RG: ", rg, ", CPF: ", cpf)
Fimalgoritmo