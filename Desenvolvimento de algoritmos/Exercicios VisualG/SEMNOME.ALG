Algoritmo "semnome";
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 21/10/2024
Var
   // Se��o de Declara��es das vari�veis
   nome, turma : caracter
   nota, soma : inteiro
   media : real

Inicio
   escreval("### CALCULADORA DE MEDIA ##")
   escreval("Informe seu nome:")
   leia (nome)
   escreval("Informe sua turma:")
   leia (turma)
   
   escreval("################")
   escreval("Informe a sua primeira nota: ")
   leia (nota)
   soma <- soma + nota
   escreval("Informe a sua segunda nota: ")
   leia (nota)
   soma <- soma + nota
   escreval("Informe a sua terceira nota: ")
   leia (nota)
   soma <- soma + nota
   escreval("Informe a sua quarta nota: ")
   leia (nota)
   soma <- soma + nota
   escreval("Informe a sua quinta nota: ")
   leia (nota)
   soma <- soma + nota
   media <- soma / 5
   
   escreval("################")
   escreval("Nome: ", nome)
   escreval("Turma: ", turma)
   escreval("M�dia: ", media)
   
Fimalgoritmo


