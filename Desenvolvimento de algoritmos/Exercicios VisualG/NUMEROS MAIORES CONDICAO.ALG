Algoritmo "Numeros Maiores condicao"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/10/2024
Var
   // Se��o de Declara��es das vari�veis
   v1, v2, v3 : inteiro

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   Escreva("Informe o primeiro n�mero: ")
   leia(v1)
   Escreva("Informe o segundo n�mero: ")
   leia(v2)
   Escreva("Informe o terceiro n�mero: ")
   leia(v3)
   Escreval()
   se(v1 > v2) e (v1 > v3)entao
      Escreval("Primeiro valor � o maior. ", v1)
   senao
      se(v2 > v1) e (v2 > v3)entao
         Escreval("Segundo valor � o maior. ", v2)
      senao
         se(v3 > v1) e (v3 > v2)entao
            Escreval("Terceiro valor � o maior. ", v3)
         senao
            se(v1 = v2) e (v1 = v3)entao
               Escreval("Os tr�s valores digitados sao iguais. ", v1, v2, v3)
            senao
               se(v1 = v2)entao
                  Escreval("O primeiro e o segundo valor s�o iguais. ", v1, v2)
               senao
                  se(v1 = v3)entao
                     Escreval("O primeiro e o terceiro valor digitado s�o iguais. ", v1, v3)
                  senao
                     escreval("O segundo e o terceiro valor s�o iguais. ", v2, v3)
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimse


Fimalgoritmo