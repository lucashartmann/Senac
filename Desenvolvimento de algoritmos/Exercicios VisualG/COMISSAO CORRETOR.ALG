Algoritmo "Comissao Corretor"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/10/2024
Var
   // Se��o de Declara��es das vari�veis
   nome : caractere
   valor, comissao : real

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   Escreva("Digite seu nome: ")
   leia(nome)
   Escreva("Digite o valor do im�vel: ")
   leia(valor)

   se (valor >= 50000) entao
      comissao <- valor * (20/100)
   senao
      se (valor >= 30000)entao
         comissao <- valor * (15/100)
      senao
         comissao <- valor * (10/100)
      fimse
   fimse
   
   Escreval("Nome do corretor: ", nome)
   Escreval("Valor do im�vel: ", valor:2:2)
   Escreval("Comiss�o do corretor: ", comissao:2:2)

Fimalgoritmo