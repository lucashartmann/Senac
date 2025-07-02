Algoritmo "Boletim com switch e notas"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 05/11/2024
Var
   // Seção de Declarações das variáveis
   nota, nota1, nota2, media : real


Inicio
   Escreval("## BOLETIM ##")
   
   escreva("Informe sua primeira nota: ")
   leia(nota)
   enquanto (nota > 10) ou (nota < 0) faca
      escreva("Informe sua primeira nota: ")
      leia(nota)
   fimenquanto
   escreva("Informe sua segunda nota: ")
   leia(nota1)
   enquanto (nota1 > 10) ou (nota1 < 0) faca
      escreva("Informe sua segunda nota: ")
      leia(nota1)
   fimenquanto
   escreva("Informe sua terceira nota: ")
   leia(nota2)
   enquanto (nota2 > 10) ou (nota2 < 0) faca
      escreva("Informe sua terceira nota: ")
      leia(nota2)
   fimenquanto

   media <- (nota+nota1+nota2) / 3

   Escreval()
   escreval("## RESULTADO DA CONSULTA ##")

   Escreval("Notas (em sequência): ", nota, ", ", nota1, ", ", nota2)
   Escreval("Média: ", media:2:2)
   Escreva("Situação curricular: ")

   escolha (media)
   caso 7 ate 10
      escreval("APROVADO")
   caso 5 ate 6.99
      escreval("RECUPERAÇÃO")
   caso 0 ate 4.99
      escreval("REPROVADO")
   fimescolha

Fimalgoritmo