Algoritmo "calculadora"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/10/2024
Var
   // Se��o de Declara��es das vari�veis
   number : inteiro
   v1, v2, operacao : real

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   Escreval("## CALCULADORA ##")
   Escreva("Informe o primeiro valor: ")
   leia(v1)
   Escreva("Informe o segundo valor: ")
   leia(v2)

   Escreval("## MENU ##")
   Escreval("Digite o n�mero correspondente � opera��o que voc� deseja: ")
   Escreval("1 -- Adi��o")
   Escreval("2 -- Subtra��o")
   Escreval("3 -- Multiplica��o")
   Escreval("4 -- Divis�o")
   leia (number)
   se(number = 1) entao
      Escreval("Voc� escolheu adi��o")
      operacao <- v1 + v2
      Escreval(v1, " +",v2, " = ",operacao)
   senao
      se(number = 2) entao
         Escreval("Voc� escolheu subtra��o")
         operacao <- v1 - v2
         Escreval(v1, " -",v2, " = ",operacao)
      senao
         se(number = 3) entao
            Escreval("Voc� escolheu multiplica��o")
            operacao <- v1 * v2
            Escreval(v1, " x",v2, " = ",operacao)
         senao
            se(number = 4) entao
               Escreval("Voc� escolheu divis�o")
               operacao <- v1 / v2
               Escreval(v1, " �",v2, " = ",operacao:2:2)
            senao
               escreval("o n�mero digitado � inv�lido!")
            fimse
         fimse
      fimse
   fimse

Fimalgoritmo