Algoritmo "matriz"


// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/11/2024

Var

   num: vetor[1..2,1..2] de inteiro
   i, j : inteiro

Inicio
   escreval("## ENTRADA: ##")
   para i de 1 ate 2 faca
      para j de 1 ate 2 faca
         escreva("Digite um n�mero na posi��o [",i,",",j,"]: ")
         leia(num[i,j])
      fimpara
   fimpara
   escreval("## DADOS: ##")
   escreval("O valor que est� na posi��o [1,1] �: ", num[1,1])
   escreval("O valor que est� na posi��o [1,2] �: ", num[1,2])
   escreval("O valor que est� na posi��o [2,1] �: ", num[2,1])
   escreval("O valor que est� na posi��o [2,2] �: ", num[2,2])
   
  // para i de 1 ate 2 faca
  //    para j de 1 ate 2 faca
  //       escreval("O valor que est� na posi��o [",i,",",j,"] �: ", num[i,j])
  //    fimpara
  // fimpara

Fimalgoritmo