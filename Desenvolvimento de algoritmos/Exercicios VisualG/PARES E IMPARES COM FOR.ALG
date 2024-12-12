Algoritmo "pares e impares com for"

// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Lucas
// Data atual  : 14/11/2024

Var

   number, i : inteiro
   divisao : real

Inicio
   escreva("Digite um número: ")
   leia(number)
   escreval()
   escreval("Números primos de 1 até ", number,":")
   para  i de 1 ate number faca
      divisao <- i % 2
      se (divisao = 0) entao
         escreval(i)
      fimse
   fimpara
   escreval()
   escreval("Números Ímpares de 1 até ", number,":")
   para  i de 1 ate number faca
      divisao <- i % 2
      se (divisao = 0) entao
      senao
         escreval(i)
      fimse
   fimpara

Fimalgoritmo