Algoritmo "Boletim com condicoes"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Lucas
// Data atual  : 29/10/2024
Var
   nome, turma : caractere
   n, n1, n2, n3, n4, media : real

Inicio
   Escreva("Digite seu nome: ")
   Leia(nome)
   Escreva("Digite sua turma: ")
   Leia(turma)
   Escreva("Digite sua primeira nota: ")
   leia(n)

   enquanto n > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua primeira nota: ")
      leia(n)
   fimenquanto

   Escreva("Digite sua segunda nota: ")
   leia(n1)
   enquanto n1 > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua segunda nota: ")
      leia(n1)
   fimenquanto

   Escreva("Digite sua terceira nota: ")
   leia(n2)
   enquanto n2 > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua terceira nota: ")
      leia(n2)
   fimenquanto

   Escreva("Digite sua quarta nota: ")
   leia(n3)
   enquanto n3 > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua quarta nota: ")
      leia(n3)
   fimenquanto

   Escreva("Digite sua quinta nota: ")
   leia(n4)
   enquanto n4 > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua quinta nota: ")
      leia(n4)
   fimenquanto

   media <- (n + n1 + n2 + n3 + n4) / 5

   Escreval("Nome do aluno: ", nome)
   Escreval("Turma do aluno: ", turma)
   Escreval("Notas do aluno (em ordem): ", n, ", ", n1, ", ", n2, ", ", n3, ", ", n4)
   Escreval("Situação curricular: ")
   se(media >= 7) e (media <= 10) entao
      Escreva("APROVADO")
   senao
      se(media >= 5) e (media < 7) entao
         Escreva("RECUPERAÇÃO")
      senao
         se(media >= 0) e (media < 5) entao
            Escreva("REPROVADO")
         senao
            se(media > 10) ou (media < 0)entao
               Escreva("FALHA NO SISTEMA!")
            fimse
         fimse
      fimse
   fimse


Fimalgoritmo