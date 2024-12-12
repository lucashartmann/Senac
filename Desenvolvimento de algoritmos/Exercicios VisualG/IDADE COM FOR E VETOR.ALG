Algoritmo "Idade com For e Vetor"
//
//
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/11/2024
Var
   // Seção de Declarações das variáveis
   idades: vetor[1..8] de inteiro
   c, soma, maior, posi : inteiro
   media : real

Inicio
   escreval("## ENTRADA DE DADOS ##")
   para c <- 1 ate 8 faca
      Escreval("Digite a idade da ", c, " pessoa")
      leia(idades[c])
      soma <- soma + idades[c]

   fimpara

   para c <- 1 ate 8 faca
      se (idades[c] > maior) entao
         maior <- idades[c]
      fimse
   fimpara

   para c <- 1 ate 8 faca
      se (idades[c] >= maior) entao
         escreval("Pessoa com mais velha na posição ", c)
      fimse
   fimpara

   escreval()
   escreval("## DADOS ##")
   media <- soma / c
   escreval("Soma: ", soma)
   escreval("Media: ", media)
   escreval("Pessoa mais velha: ", maior)

Fimalgoritmo