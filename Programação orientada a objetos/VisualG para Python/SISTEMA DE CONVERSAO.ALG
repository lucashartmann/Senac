Algoritmo "Sistema de conversao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/10/2024
Var
   reais, dolar, cotacao_dolar: real

Inicio
   Escreval("## Sistema de conversão de reais para dolar")
   cotacao_dolar <- 5,71
   Escreval("Informe o valor para a conversão:")
   leia (reais)
   Escreval("Informe a cotação atual do dolar:")
   leia(cotacao_dolar)
   dolar <- reais / cotacao_dolar
   Escreval("Sua quantidade de dolar: ", dolar:2:2)
   escreval()

   Escreval("## Sistema de conversão de dolar para reais")
   Escreval("Informe o valor para a conversão:")
   leia (dolar)
   Escreval("Informe a cotação atual do dolar:")
   leia(cotacao_dolar)
   reais <- dolar * cotacao_dolar
   Escreval("Sua quantidade de reais: ", reais:2:2)
   escreval()

Fimalgoritmo