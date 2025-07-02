Algoritmo "Condicoes"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Lucas
// Data atual  : 23/10/2024
Var

   numero : inteiro

Inicio

   escreval("## JOGO DO TIGRINHO ##")
   escreval("Digite um número")
   leia (numero)
   se (numero = 10) entao
      escreval("Parabéns, você ganhou!!!")
   senao
      escreval("Infelizmente você não ganhou. Tente novamente")
   fimse

   escreval()

   Escreval("## Múltiplos ##")
   se(numero mod 2 = 0) entao
      escreval("É múltiplo de dois")
   senao("Não é múltiplo de dois")
   fimse

Fimalgoritmo