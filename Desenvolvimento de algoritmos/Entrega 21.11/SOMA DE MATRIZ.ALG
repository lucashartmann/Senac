Algoritmo "Soma de valores da Matriz"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Descri��o   :
// Autor(a)    : Lucas
// Data atual  : 21/11/2024
Var
   // Se��o de Declara��es das vari�veis
   matrix: vetor[1..2,1..2] de inteiro
   vector: vetor[1..10] de inteiro
   soma : inteiro
   i, j : inteiro

Inicio

   escreval("## ENTRADA DE DADOS: ##")

   para i de 1 ate 2 faca
      para j de 1 ate 2 faca
         escreva("Digite um n�mero na posi��o [",i,",",j,"]: ")
         leia(matrix[i,j])
      fimpara
   fimpara

   para j de 1 ate 2 faca
      para i de 1 ate 2 faca
         soma <- soma + matrix[i][j]
      fimpara
   fimpara

   escreval()
   escreval("## DADOS: ##")
   para i de 1 ate 2 faca
      para j de 1 ate 2 faca
         escreval("O valor que est� na posi��o [",i,",",j,"] �: ", matrix[i,j])
      fimpara
   fimpara
   escreval("Soma: ", soma)



Fimalgoritmo