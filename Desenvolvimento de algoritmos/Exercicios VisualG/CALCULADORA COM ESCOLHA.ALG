Algoritmo "calculadora com escolha"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
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
      Escreval("Digite a opera��o correspondente � opera��o que voc� deseja: ")
      Escreval("+ -- Adi��o")
      Escreval("- -- Subtra��o")
      Escreval("* -- Multiplica��o")
      Escreval("/ -- Divis�o")
      leia (operacao)

      escolha operacao
      caso "+"
         Escreval("Voc� escolheu adi��o")
         resultado <- v1 + v2
         condicao <- 1
      caso "-"
         Escreval("Voc� escolheu subtra��o")
         resultado <- v1 - v2
         condicao <- 1
      caso "*"
         Escreval("Voc� escolheu multiplica��o")
         resultado <- v1 * v2
         condicao <- 1
      caso "/"
         Escreval("Voc� escolheu divis�o")
         resultado <- v1 / v2
         condicao <- 1
      outrocaso
         escreval("A opera��o digitada � inv�lida!")
         condicao <- 0
      fimescolha
   fimenquanto

   Escreval(v1, "", operacao, "", v2, " = ", resultado:2:1)
Fimalgoritmo