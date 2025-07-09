Algoritmo "BAR"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   :
// Autor(a)    : Lucas
// Data atual  : 21/11/2024
Var

   nomeBebidas: vetor [1..10] de caractere
   quantBebidas, i, j, maxContagem, contagemAtual: inteiro
   maisPedida, empate : caractere

Inicio
   Escreval("### SISTEMA DO BAR DO ITO ###")
   escreva("Quantas bebidas foram pedidas? (Máximo 10) ")
   leia(quantBebidas)

   se(quantBebidas > 10) entao
      quantBebidas <- 10
   fimse

   para i de 1 ate quantBebidas faca
      escreva("Informe o nome da bebida pedida: ")
      leia(nomeBebidas[i])
   fimpara

   maxContagem <- 0
   maisPedida <- ""
   empate <- "False"

   para i de 1 ate quantBebidas faca
      contagemAtual <- 0
      para j de 1 ate quantBebidas faca
         se (nomeBebidas[i] = nomeBebidas[j]) entao
            contagemAtual <- contagemAtual + 1
         fimse
      fimpara
      se (contagemAtual > maxContagem) entao
         maxContagem <- contagemAtual
         maisPedida <- nomeBebidas[i]
         empate <- "False"
      senao
         se ((contagemAtual = maxContagem) e (nomeBebidas[i] <> maisPedida)) entao
            empate <- "True"
         fimse
      fimse
   fimpara

   se((maxContagem > 1) e (empate = "False")) entao
      escreval("A bebida mais pedida foi: ", maisPedida, " com ", maxContagem, " pedidos.")
   senao
      escreval("Não teve uma bebida mais pedida.")
   fimse

Fimalgoritmo