Algoritmo "OperacoesBasicas"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 21/10/2024

Var
   valorUm, valorDois : inteiro
   resultado : real

Inicio

   Escreval("## OPERAÇÕES ##")
   Escreval("Informe um valor")
   leia (valorUm)
   Escreval("Informe outro valor")
   leia(valorDois)
   
   Escreval("########")
   
   resultado <- valorUm + valorDois
   Escreval("Soma: ", resultado)
   
   resultado <- valorUm - valorDois
   Escreval("Subtração: ", resultado)
   
   resultado <- valorUm / valorDois
   Escreval("Divisão: ", resultado:2:2)
   
   resultado <- valorUm * valorDois
   Escreval("Multiplicação: ", resultado)
   
   resultado <- valorUm ^ valorDois
   Escreval("Potência: ", resultado)
   
   Escreval("Raiz do primeiro valor: ", Raizq(valorUm):2:2)
   Escreval("Raiz do segundo valor: ", Raizq(valorDois):2:2)


Fimalgoritmo