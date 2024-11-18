Algoritmo "boletim com for e vetor"

// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/11/2024

Var

   notas: vetor[1..5] de inteiro
   media : real
   nome, turma : caractere
   i : inteiro

Inicio
   escreval("## BOLETIM ##")
   escreva("Informe o nome do aluno: ")
   leia(nome)
   escreva("Informe a turma do aluno: ")
   leia(turma)

   para i de 1 ate 5 faca
      escreva("Digite a ", i, "° nota: ")
      leia(notas[i])
   fimpara

   media <- (notas[1] + notas[2] + notas[3] + notas[4] + notas[5]) / 5

   escreval()
   escreval("## RESULTADOS ##")
   escreval("Nome do aluno: ", nome)
   escreval("Turma do aluno: ", turma)
   escreva("Notas em ordem: ")
   para i de 1 ate 5 faca
      escreva(notas[i], "")
   fimpara
   //para i de 1 ate 5 faca
   //   escreva(i, "° nota: ", notas[i])
   //fimpara
   escreval()
   escreval("Média: ", media)

Fimalgoritmo