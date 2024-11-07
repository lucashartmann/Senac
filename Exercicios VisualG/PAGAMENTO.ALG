Algoritmo "pagamento"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Lucas
// Data atual  : 05/11/2024
Var

   nome : caractere
   valorInicial, valorTotal : real
   opcao,desconto, acrescimo, condicao : inteiro

Inicio

   Escreva("Digite seu nome: ")
   leia(nome)
   Escreva("Digite o valor da venda: ")
   leia(valorInicial)
   enquanto condicao = 0 faca
      Escreval("## MENU PAGAMENTO ##")
      Escreval("Digite o número da operação desejada: ")
      Escreval("1 -- Venda a vista (10% de desconto)")
      Escreval("2 -- Venda a prazo de 30 dias (5% de desconto)")
      Escreval("3 -- Venda a prazo de 60 dias")
      Escreval("4 -- Venda a prazo de 90 dias (5% de acréscimo)")
      Escreval("5 -- Venda com cartão de débito (8% de desconto)")
      Escreval("6 -- Venda com cartão de crédito (7% de desconto)")
      leia(opcao)
      escolha(opcao)
      caso 1
         desconto <- 10
         valorTotal <- valorInicial - (valorInicial * (desconto/100))
         condicao <- 1
      caso 2
         desconto <- 5
         valorTotal <- valorInicial - (valorInicial * (desconto/100))
         condicao <- 1
      caso 3
         valorTotal <- valorInicial
         condicao <- 1
      caso 4
         acrescimo <- 5
         valorTotal <- valorInicial + (valorInicial * (acrescimo/100))
         condicao <- 1
      caso 5
         desconto <- 8
         valorTotal <- valorInicial - (valorInicial * (desconto/100))
         condicao <- 1
      caso 6
         desconto <- 7
         valorTotal <- valorInicial - (valorInicial * (desconto/100)
         condicao <- 1
      outrocaso
         escreval("Número digitado inválido. Tente novamente")
      fimescolha
   fimenquanto


   Escreval("Nome do vendedor: ", nome)
   Escreval("Valor da venda: ", valorInicial:2:1)
   se (desconto > 0) entao
      Escreval("Desconto: ", desconto, "%")
   senao
      se(acrescimo > 0) entao
         Escreval("Acréscimo: ", acrescimo, "%")
      fimse
   fimse
   Escreval("Valor total da venda: ", valorTotal:2:1)


Fimalgoritmo