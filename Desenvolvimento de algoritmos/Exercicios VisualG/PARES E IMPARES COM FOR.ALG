Algoritmo "pares e impares com for"

// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Lucas
// Data atual  : 14/11/2024

Var

   number, i : inteiro
   divisao : real

Inicio
   escreva("Digite um n�mero: ")
   leia(number)
   escreval()
   escreval("N�meros primos de 1 at� ", number,":")
   para  i de 1 ate number faca
      divisao <- i % 2
      se (divisao = 0) entao
         escreval(i)
      fimse
   fimpara
   escreval()
   escreval("N�meros �mpares de 1 at� ", number,":")
   para  i de 1 ate number faca
      divisao <- i % 2
      se (divisao = 0) entao
      senao
         escreval(i)
      fimse
   fimpara

Fimalgoritmo