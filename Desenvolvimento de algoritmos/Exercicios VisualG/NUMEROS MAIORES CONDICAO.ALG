Algoritmo "Numeros Maiores condicao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/10/2024
Var
   // Seção de Declarações das variáveis
   v1, v2, v3 : inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva("Informe o primeiro número: ")
   leia(v1)
   Escreva("Informe o segundo número: ")
   leia(v2)
   Escreva("Informe o terceiro número: ")
   leia(v3)
   Escreval()
   se(v1 > v2) e (v1 > v3)entao
      Escreval("Primeiro valor é o maior. ", v1)
   senao
      se(v2 > v1) e (v2 > v3)entao
         Escreval("Segundo valor é o maior. ", v2)
      senao
         se(v3 > v1) e (v3 > v2)entao
            Escreval("Terceiro valor é o maior. ", v3)
         senao
            se(v1 = v2) e (v1 = v3)entao
               Escreval("Os três valores digitados sao iguais. ", v1, v2, v3)
            senao
               se(v1 = v2)entao
                  Escreval("O primeiro e o segundo valor são iguais. ", v1, v2)
               senao
                  se(v1 = v3)entao
                     Escreval("O primeiro e o terceiro valor digitado são iguais. ", v1, v3)
                  senao
                     escreval("O segundo e o terceiro valor são iguais. ", v2, v3)
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimse


Fimalgoritmo