Algoritmo "Funcao Dobro"
//
//
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/11/2024
Var
   // Seção de Declarações das variáveis
   numero, resultado : real

funcao Dobro(valor : real) : real
var
   total : real
inicio
   total <- valor * 2
   retorne total
fimfuncao

Inicio
   escreva("Informe um número: ")
   leia(numero)
   resultado <- Dobro(numero)
   escreval("#################")
   escreval("Dobro do número digitado: ", resultado)

Fimalgoritmo