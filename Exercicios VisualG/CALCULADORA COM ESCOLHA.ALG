Algoritmo "calculadora com escolha"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/11/2024
Var

   v1, v2, resultado : real
   operacao : caractere
   condicao : inteiro
Inicio

   condicao <- 0
   Escreval("## CALCULADORA ##")
   Escreva("Informe o primeiro valor: ")
   leia(v1)
   Escreva("Informe o segundo valor: ")
   leia(v2)

   enquanto condicao = 0 faca
      Escreval("## MENU ##")
      Escreval("Digite a operação correspondente á operação que você deseja: ")
      Escreval("+ -- Adição")
      Escreval("- -- Subtração")
      Escreval("* -- Multiplicação")
      Escreval("/ -- Divisão")
      leia (operacao)

      escolha operacao
      caso "+"
         Escreval("Você escolheu adição")
         resultado <- v1 + v2
         condicao <- 1
      caso "-"
         Escreval("Você escolheu subtração")
         resultado <- v1 - v2
         condicao <- 1
      caso "*"
         Escreval("Você escolheu multiplicação")
         resultado <- v1 * v2
         condicao <- 1
      caso "/"
         Escreval("Você escolheu divisão")
         resultado <- v1 / v2
         condicao <- 1
      outrocaso
         escreval("A operação digitada é inválida!")
         condicao <- 0
      fimescolha
   fimenquanto

   Escreval(v1, "", operacao, "", v2, " = ", resultado:2:1)
Fimalgoritmo