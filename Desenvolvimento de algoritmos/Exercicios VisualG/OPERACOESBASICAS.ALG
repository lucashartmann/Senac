Algoritmo "OperacoesBasicas"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 21/10/2024

Var
   valorUm, valorDois : inteiro
   resultado : real

Inicio

   Escreval("## OPERA��ES ##")
   Escreval("Informe um valor")
   leia (valorUm)
   Escreval("Informe outro valor")
   leia(valorDois)
   
   Escreval("########")
   
   resultado <- valorUm + valorDois
   Escreval("Soma: ", resultado)
   
   resultado <- valorUm - valorDois
   Escreval("Subtra��o: ", resultado)
   
   resultado <- valorUm / valorDois
   Escreval("Divis�o: ", resultado:2:2)
   
   resultado <- valorUm * valorDois
   Escreval("Multiplica��o: ", resultado)
   
   resultado <- valorUm ^ valorDois
   Escreval("Pot�ncia: ", resultado)
   
   Escreval("Raiz do primeiro valor: ", Raizq(valorUm):2:2)
   Escreval("Raiz do segundo valor: ", Raizq(valorDois):2:2)


Fimalgoritmo