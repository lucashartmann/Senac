Algoritmo "boletim com condicao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/10/2024
Var

   nome, turma : caractere
   nota1, nota2, nota3, nota4, nota5, media, soma : real

Inicio

   escreval("### BOLETIM ###")
   escreva("Informe seu nome: ")
   leia(nome)
   escreva("Informe sua turma: ")
   leia(turma)
   escreva("Informe sua primeira nota: ")
   leia(nota1)
   escreva("Informe sua segunda nota: ")
   leia(nota2)
   escreva("Informe sua terceira nota: ")
   leia(nota3)
   escreva("Informe sua quarta nota: ")
   leia(nota4)
   escreva("Informe sua quinta nota: ")
   leia(nota5)
   soma <- nota1 + nota2 + nota3 + nota4 + nota5
   media <- soma / 5
   escreval()

   escreval("### Resultado ###")
   escreval("Nome do aluno: ", nome)
   escreval("Turma do aluno: ", turma)
   escreval ("Notas: ", nota1, ", ", nota2, ", ", nota3, ", ", nota4, ", ", nota5)
   escreval("Média do aluno: ", media)
   se (media >= 7) entao
      escreval("Parabéns, você foi aprovado!")
   senao
      escreval("Você foi reprovado!")
   fimse



Fimalgoritmo