Algoritmo "calculadora"

// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Descri��o   :
// Autor(a)    : Lucas
// Data atual  : 21/11/2024

Var

   n, n1 : real
   number : inteiro

funcao adicao(n, n1 : real) : real
var
   total : real
inicio
   total <- (n + n1)
   retorne total
fimfuncao
funcao subtracao(n, n1 : real) : real
var
   total : real
inicio
   se(n > n1) entao
      total <- (n - n1)
   senao
      total <- (n1 - n)
   fimse
   retorne total
fimfuncao
funcao divisao(n, n1 : real) : real
var
   total : real
inicio
   total <- (n / n1)
   retorne total
fimfuncao
funcao multiplicacao(n, n1 : real) : real
var
   total : real
inicio
   total <- (n * n1)
   retorne total
fimfuncao

Inicio
   escreval("## CALCULADORA ##")
   escreva("Informe o primeiro valor: ")
   leia(n)
   escreva("Informe o primeiro valor: ")
   leia(n1)

   escreval()
   escreval("Opera��es disponiveis:")
   escreval("1 -- Adi��o")
   escreval("2 -- Subtra��o")
   escreval("3 -- Divis�o")
   escreval("4 -- Multiplica��o")
   escreva("Digite o n�mero da opera��o desejada: ")
   leia(number)
   escolha(number)
      escreval()
   caso 1
      escreva(n, " + ", n1 , " = " )
      escreval(adicao(n, n1))
   caso 2
      escreva(n, " - ", n1 , " = " )
      escreval(subtracao(n, n1))
   caso 3
      escreva(n, " / ", n1 , " = " )
      escreval(divisao(n, n1):2:2)
   caso 4
      escreva(n, " * ", n1 , " = " )
      escreval(multiplicacao(n, n1):2:2)
   outrocaso
      escreval("Voc� digitou uma opera��o inv�lida")
   fimescolha

Fimalgoritmo