Algoritmo "escolinha com switch"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 04/11/2024
Var
   // Seção de Declarações das variáveis
   nome, categoria : caractere
   idade : inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva("Informe seu nome: ")
   leia(nome)
   Escreva("Informe sua idade: ")
   leia(idade)
   se (idade > 25) ou (idade < 5) entao
      escreval("Idade inválida, tente novamente")
   senao
      escolha(idade)
      caso 5 ate 10
         categoria <- "infantil"
      caso 11 ate 15
         categoria <- "juvenil"
      caso 16 ate 20
         categoria <- "junior"
      caso 21 ate 25
         categoria <- "profissional"
      fimescolha
      Escreval("Nome: ", nome)
      Escreval("Idade: ", idade)
      Escreval("Categoria: ", categoria)
   fimse
   
Fimalgoritmo