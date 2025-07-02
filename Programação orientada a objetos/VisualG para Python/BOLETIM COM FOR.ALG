Algoritmo "Boletim com FOR"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Autor(a)    : Lucas
// Data atual  : 13/11/2024

Var

   i, quant : inteiro
   nome, turma : caractere
   nota,nota1,nota2 : inteiro
   media : real

Inicio
   escreval("##### BOLETIM ######")
   escreva("Informe a quantidade de registros que deseja informar: ")
   leia(quant)
   para  i de 1 ate quant faca
      escreval()
      escreval("------------- Entrada de Dados ------------")
      escreva("Informe o nome do Aluno: ")
      leia(nome)
      escreva("Informe a turma do Aluno: ")
      leia(turma)
      escreva("Informe a primeira nota do Aluno: ")
      leia(nota)
      escreva("Informe a segunda nota do Aluno: ")
      leia(nota1)
      escreva("Informe a terceira nota do Aluno: ")
      leia(nota2)
      media <- ((nota + nota1 + nota2) / 3)
      escreval()
      escreval("Nome do aluno: ", nome)
      escreval("Turma do aluno: ", turma)
      escreval("Notas do aluno em sequência: ", nota, ", ", nota1, ", ", nota2)
      escreval("Média final: ", media:2:1)
      escreva("Situação final do aluno: ")
      se (media >= 7) entao
         escreval("Aprovado!")
      senao
         se(media >= 5) entao
            escreval("Recuperação")
         senao
            escreval("Reprovado!")
         fimse
      fimse
   fimpara


Fimalgoritmo