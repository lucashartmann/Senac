Algoritmo "Funcao Dobro"
//
//
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/11/2024
Var
   // Se��o de Declara��es das vari�veis
   numero, resultado : real

funcao Dobro(valor : real) : real
var
   total : real
inicio
   total <- valor * 2
   retorne total
fimfuncao

Inicio
   escreva("Informe um n�mero: ")
   leia(numero)
   resultado <- Dobro(numero)
   escreval("#################")
   escreval("Dobro do n�mero digitado: ", resultado)

Fimalgoritmo