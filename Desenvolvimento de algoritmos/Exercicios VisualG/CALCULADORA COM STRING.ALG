Algoritmo "calculadora com String"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/11/2024
Var
   // Seção de Declarações das variáveis
   v1, v2, resultado : real
   operacao : caractere

Inicio
   Escreval("## CALCULADORA ##")
   Escreva("Informe o primeiro valor: ")
   leia(v1)
   Escreva("Informe o segundo valor: ")
   leia(v2)

   Escreval("## MENU ##")
   Escreval("Informe a operação correspondente á operação que você deseja: ")
   Escreval("+ -- Adição")
   Escreval("- -- Subtração")
   Escreval("* -- Multiplicação")
   Escreval("/ -- Divisão")
   leia (operacao)
   
   se((operacao = "+")ou(operacao = "-")ou(operacao = "*")ou(operacao = "/")) entao
      se(operacao = "+") entao
         Escreval("Você escolheu adição")
         resultado <- v1 + v2
      senao
         se(operacao = "-") entao
            Escreval("Você escolheu subtração")
            resultado <- v1 - v2
         senao
            se(operacao = "*") entao
               Escreval("Você escolheu multiplicação")
               resultado <- v1 * v2
            senao
               se(operacao = "/") entao
                  Escreval("Você escolheu divisão")
                  resultado <- v1 / v2
               fimse
            fimse
         fimse
      fimse
      escreval(v1,"",operacao,"",v2," = ", resultado:2:1)
   senao
      escreval("Operação inválida")
      escreval("Tente novamente!")
   fimse
   
Fimalgoritmo