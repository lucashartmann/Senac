Algoritmo "BAR"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   :
// Autor(a)    : Lucas
// Data atual  : 21/11/2024
Var

   nomeBebidas: vetor [1..10] de caractere
   quantBebidas, i, j, maxContagem, contagemAtual: inteiro
   maisPedida : caractere


Inicio
   Escreval("### SISTEMA DO BAR DO ITO ###")

   escreva("Quantas bebidas foram pedidas? ")
   leia(quantBebidas)

   se(quantBebidas > 10) entao
      quantBebidas < 10
   fimse

   para i de 1 ate quantBebidas faca
      escreva("Informe o nome da bebida pedida: ")
      leia(nomeBebidas[i])
   fimpara

   maxContagem <- 0
   maisPedida <- ""

   para i de 1 ate 10 faca
      contagemAtual <- 0

      para j de 1 ate 10 faca
         se (nomeBebidas[i] = nomeBebidas[j]) entao
            contagemAtual <- contagemAtual + 1
         fimse
      fimpara

      se (contagemAtual > maxContagem) entao
         maxContagem <- contagemAtual
         maisPedida <- nomeBebidas[i]
      fimse
   fimpara

   se(maxContagem > 1) entao
      escreval("A bebida mais pedida foi: ", maisPedida)
   senao
      escreval("As bebidas não foram repetidas")
   fimse

Fimalgoritmo