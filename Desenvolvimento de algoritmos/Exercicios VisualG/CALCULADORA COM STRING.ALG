Algoritmo "calculadora com String"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/11/2024
Var
   // Se��o de Declara��es das vari�veis
   v1, v2, resultado : real
   operacao : caractere

Inicio
   Escreval("## CALCULADORA ##")
   Escreva("Informe o primeiro valor: ")
   leia(v1)
   Escreva("Informe o segundo valor: ")
   leia(v2)

   Escreval("## MENU ##")
   Escreval("Informe a opera��o correspondente � opera��o que voc� deseja: ")
   Escreval("+ -- Adi��o")
   Escreval("- -- Subtra��o")
   Escreval("* -- Multiplica��o")
   Escreval("/ -- Divis�o")
   leia (operacao)
   
   se((operacao = "+")ou(operacao = "-")ou(operacao = "*")ou(operacao = "/")) entao
      se(operacao = "+") entao
         Escreval("Voc� escolheu adi��o")
         resultado <- v1 + v2
      senao
         se(operacao = "-") entao
            Escreval("Voc� escolheu subtra��o")
            resultado <- v1 - v2
         senao
            se(operacao = "*") entao
               Escreval("Voc� escolheu multiplica��o")
               resultado <- v1 * v2
            senao
               se(operacao = "/") entao
                  Escreval("Voc� escolheu divis�o")
                  resultado <- v1 / v2
               fimse
            fimse
         fimse
      fimse
      escreval(v1,"",operacao,"",v2," = ", resultado:2:1)
   senao
      escreval("Opera��o inv�lida")
      escreval("Tente novamente!")
   fimse
   
Fimalgoritmo