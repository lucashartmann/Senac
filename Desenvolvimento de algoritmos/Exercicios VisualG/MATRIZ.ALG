Algoritmo "matriz"


// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/11/2024

Var

   num: vetor[1..2,1..2] de inteiro
   i, j : inteiro

Inicio
   escreval("## ENTRADA: ##")
   para i de 1 ate 2 faca
      para j de 1 ate 2 faca
         escreva("Digite um número na posição [",i,",",j,"]: ")
         leia(num[i,j])
      fimpara
   fimpara
   escreval("## DADOS: ##")
   escreval("O valor que está na posição [1,1] é: ", num[1,1])
   escreval("O valor que está na posição [1,2] é: ", num[1,2])
   escreval("O valor que está na posição [2,1] é: ", num[2,1])
   escreval("O valor que está na posição [2,2] é: ", num[2,2])
   
  // para i de 1 ate 2 faca
  //    para j de 1 ate 2 faca
  //       escreval("O valor que está na posição [",i,",",j,"] é: ", num[i,j])
  //    fimpara
  // fimpara

Fimalgoritmo