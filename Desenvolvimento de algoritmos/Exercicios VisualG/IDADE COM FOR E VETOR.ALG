Algoritmo "Idade com For e Vetor"
//
//
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/11/2024
Var
   // Se��o de Declara��es das vari�veis
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
         escreval("Pessoa com mais velha na posi��o ", c)
      fimse
   fimpara

   escreval()
   escreval("## DADOS ##")
   media <- soma / c
   escreval("Soma: ", soma)
   escreval("Media: ", media)
   escreval("Pessoa mais velha: ", maior)

Fimalgoritmo