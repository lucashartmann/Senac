Algoritmo "calculadora"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/10/2024
Var
   // Seção de Declarações das variáveis
   number : inteiro
   v1, v2, operacao : real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreval("## CALCULADORA ##")
   Escreva("Informe o primeiro valor: ")
   leia(v1)
   Escreva("Informe o segundo valor: ")
   leia(v2)

   Escreval("## MENU ##")
   Escreval("Digite o número correspondente á operação que você deseja: ")
   Escreval("1 -- Adição")
   Escreval("2 -- Subtração")
   Escreval("3 -- Multiplicação")
   Escreval("4 -- Divisão")
   leia (number)
   se(number = 1) entao
      Escreval("Você escolheu adição")
      operacao <- v1 + v2
      Escreval(v1, " +",v2, " = ",operacao)
   senao
      se(number = 2) entao
         Escreval("Você escolheu subtração")
         operacao <- v1 - v2
         Escreval(v1, " -",v2, " = ",operacao)
      senao
         se(number = 3) entao
            Escreval("Você escolheu multiplicação")
            operacao <- v1 * v2
            Escreval(v1, " x",v2, " = ",operacao)
         senao
            se(number = 4) entao
               Escreval("Você escolheu divisão")
               operacao <- v1 / v2
               Escreval(v1, " ÷",v2, " = ",operacao:2:2)
            senao
               escreval("o número digitado é inválido!")
            fimse
         fimse
      fimse
   fimse

Fimalgoritmo