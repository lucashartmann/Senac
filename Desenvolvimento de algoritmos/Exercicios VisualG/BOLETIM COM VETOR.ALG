Algoritmo "Boletim com Vetor"

// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/11/2024
Var

   // Seção de Declarações das variáveis
   nome, turma : caractere
   media : real
   notas:vetor[1..5] de inteiro

Inicio
   escreval("##### BOLETIM ####")

   Escreva("Digite seu nome: ")
   Leia(nome)
   Escreva("Digite sua turma: ")
   Leia(turma)

   Escreva("Digite sua primeira nota: ")
   leia(notas[1])
   enquanto notas[1] > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua primeira nota: ")
      leia(notas[1])
   fimenquanto

   Escreva("Digite sua segunda nota: ")
   leia(notas[2])
   enquanto notas[2] > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua segunda nota: ")
      leia(notas[2])
   fimenquanto

   Escreva("Digite sua terceira nota: ")
   leia(notas[3])
   enquanto notas[3] > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua terceira nota: ")
      leia(notas[3])
   fimenquanto

   Escreva("Digite sua quarta nota: ")
   leia(notas[4])
   enquanto notas[4] > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua quarta nota: ")
      leia(notas[4])
   fimenquanto

   Escreva("Digite sua quinta nota: ")
   leia(notas[5])
   enquanto notas[5] > 10 faca
      Escreval("Nota não pode ser maior que 10")
      Escreva("Digite sua quinta nota: ")
      leia(notas[5])
   fimenquanto

   media <- (notas[1] + notas[2] + notas[3] + notas[4] + notas[5]) / 5

   Escreval("Nome do aluno: ", nome)
   Escreval("Turma do aluno: ", turma)
   Escreval("Notas do aluno (em ordem): ", notas[1], ", ", notas[2], ", ", notas[3], ", ", notas[4], ", ", notas[5])
   Escreval("Média do aluno: ", media)
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