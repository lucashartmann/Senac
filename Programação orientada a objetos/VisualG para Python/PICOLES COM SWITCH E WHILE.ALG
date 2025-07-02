Algoritmo "Picoles com switch e while"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/10/2024
Var
   quantidade, quantidadeTotal, number, number2, desconto, parcelas, acrescimo : inteiro
   valorTotal, picoleValue, valorFinal: real
   condicao : caractere

Inicio
   condicao <- "s"
   Escreval("#### VENDA DE PICOLÉS ####")
   enquanto ((condicao = "s") ou (condicao = "S")) faca
      Escreval("#### MENU ####")
      Escreval("1 -- Picolé de Uva (R$1,00)")
      Escreval("2 -- Picolé de Laranja (R$1,25)")
      Escreval("3 -- Picolé de Milho (R$1,50)")
      Escreval("4 -- Picolé de Coco queimado (R$1,80)")
      Escreval("5 -- Picolé de Tamarindo (R$2,00)")
      Escreval("Digite o número correspondente ao picolé que você deseja: ")
      leia (number)
      //enquanto (number < 0) ou (number > 5) faca
      //   escreval("Número digitado incorreto. Tente novamente")
      //   Escreval("Digite o número correspondente ao picolé que você deseja: ")
      //   leia (number)
      //fimenquanto
      escolha(number)
      Caso 1
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.00)
         picoleValue <- quantidade * 1.00
         escreval("###############")
         Escreval("Quantidade de picolés de Uva comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Uva: R$", picoleValue)
      Caso 2
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.25)
         picoleValue <- quantidade * 1.25
         escreval("###############")
         Escreval("Quantidade de picolés de Laranja comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Laranja: R$", picoleValue)
      Caso 3
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.50)
         picoleValue <- quantidade * 1.50
         escreval("###############")
         Escreval("Quantidade de picolés de Milho comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Milho: R$", picoleValue)
      Caso 4
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.80)
         picoleValue <- quantidade * 1.80
         escreval("###############")
         Escreval("Quantidade de picolés de Coco queimado comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Coco queimado: R$", picoleValue)
      Caso 5
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 2.00)
         picoleValue <- quantidade * 2.00
         escreval("###############")
         Escreval("Quantidade de picolés de Tamarindo comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Tamarindo: R$", picoleValue)
      outrocaso
         escreval("numero digitado incorreto. Tente novamente")
      fimescolha

      escreval()
      escreval("###############")
      Escreval("Quantidade de picolés comprados no total: ", quantidadeTotal)
      Escreval("Valor a ser pago no total: R$", valorTotal)
      escreval()
      escreval("Deseja seguir comprando? (S/N) ")
      leia(condicao)
   fimenquanto

   number2 <- 1
   enquanto (number2 < 0) ou (number2 > 6) faca
      Escreval("#### CAIXA ####")
      Escreval("1 -- A vista em dinheiro ou PIX (10% OFF)")
      Escreval("2 -- No cartao de débito (5% OFF)")
      Escreval("3 -- No cartao de credito em 1x")
      Escreval("4 -- No cartao de credito em 2x (+5% acréscimo)")
      Escreval("5 -- No cartao de credito em 3x (+10% acréscimo)")
      Escreval("6 -- No cartao de credito em 4x (+15% acréscimo)")
      Escreval("Digite o número correspondente á forma de pagamento: ")
      leia (number2)
   fimenquanto
   escolha(number2)
   caso 1
      desconto <- 10
      valorFinal <- valorTotal - (valorTotal * 0.10)
   caso 2
      desconto <- 10
      valorFinal <- valorTotal - (valorTotal * 0.05)
   caso 3
   caso 4
      parcelas <- 2
      acrescimo <- 5
      valorFinal <- valorTotal + (valorTotal * 0.05)
   caso 5
      parcelas <- 3
      acrescimo <- 10
      valorFinal <- valorTotal + (valorTotal * 0.10)
   caso 6
      parcelas <- 4
      acrescimo <- 15
      valorFinal <- valorTotal + (valorTotal * 0.15)
   outrocaso
      ESCREVA("o número digitado é inválido! Tente novamente")
   fimescolha

   escreval()
   Escreval("#### RECIBO #####")
   Escreval("Quantidade de picolés comprados: ", quantidadeTotal)
   Escreval("Valor total: R$", valorTotal)
   Escreval("Desconto: ", desconto)
   Escreval("Acréscimo: ", acrescimo)
   Escreval("Número de parcelas: ", parcelas)
   Escreval("Valor final pago: R$", valorTotal)

Fimalgoritmo