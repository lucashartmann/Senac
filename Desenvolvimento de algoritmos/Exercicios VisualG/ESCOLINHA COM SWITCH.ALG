Algoritmo "escolinha com switch"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 04/11/2024
Var
   // Se��o de Declara��es das vari�veis
   nome, categoria : caractere
   idade : inteiro

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   Escreva("Informe seu nome: ")
   leia(nome)
   Escreva("Informe sua idade: ")
   leia(idade)
   se (idade > 25) ou (idade < 5) entao
      escreval("Idade inv�lida, tente novamente")
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