Algoritmo "Lucas Hartmann - Loja de Picolés"
// Disciplina   : [Linguagem e Lï¿½gica de Programaï¿½ï¿½o]
// Professor   : Miguel
// Autor(a)    : Lucas
// Data atual  : 31/10/2024
Var
   quantidade, quantidadeTotal, number, number2, quantidadeAtual : inteiro
   desconto, parcelas, acrescimo : inteiro
   descontoTotal, parcelasTotal, acrescimoTotal : inteiro
   valorTotal, picoleValue, valorFinal, valorParcelado, valorAtual: real
   condicao, condicao2 : caractere
   valorParceladoTotal, valorFinalAtual: real

Inicio
   condicao <- "s"
   condicao2 <- "s"
   number <- 0

   enquanto ((condicao2 = "s") ou (condicao2 = "S")) faca
      enquanto ((condicao = "s") ou (condicao = "S")) faca
         enquanto (number <= 0) ou (number > 6) faca
            Escreval("#### VENDA DE PICOLÉS ####")
            escreval()
            Escreval("#### MENU ####")
            Escreval("1 -- Picolé de Uva (R$1,00)")
            Escreval("2 -- Picolé de Laranja (R$1,25)")
            Escreval("3 -- Picolé de Milho (R$1,50)")
            Escreval("4 -- Picolé de Coco queimado (R$1,80)")
            Escreval("5 -- Picolé de Tamarindo (R$2,00)")
            escreval("6 -- Encerrar Programa")
            Escreval("Digite o número correspondente ao picolés que você deseja: ")
            leia (number)
            escolha(number)
            Caso 1
               Escreval("Quantos picolés deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.00)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.00)
               picoleValue <- quantidade * 1.00
               escreval("###############")
               Escreval("Quantidade de picolés de Uva comprado(s): ", quantidade)
               escreval("Valor gasto com picolés de Uva: R$", picoleValue)
            Caso 2
               Escreval("Quantos picolés deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.25)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.25)
               picoleValue <- quantidade * 1.25
               escreval("###############")
               Escreval("Quantidade de picolés de Laranja comprado(s): ", quantidade)
               escreval("Valor gasto com picolés de Laranja: R$", picoleValue)
            Caso 3
               Escreval("Quantos picolés deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.50)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.50)
               picoleValue <- quantidade * 1.50
               escreval("###############")
               Escreval("Quantidade de picolés de Milho comprado(s): ", quantidade)
               escreval("Valor gasto com picolés de Milho: R$", picoleValue)
            Caso 4
               Escreval("Quantos picolés deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 1.80)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 1.80)
               picoleValue <- quantidade * 1.80
               escreval("###############")
               Escreval("Quantidade de picolés de Coco queimado comprado(s): ", quantidade)
               escreval("Valor gasto com picolés de Coco queimado: R$", picoleValue)
            Caso 5
               Escreval("Quantos picolés deseja comprar?")
               leia(quantidade)
               quantidadeAtual <- quantidadeAtual + quantidade
               valorAtual <- valorAtual + (quantidade * 2.00)
               quantidadeTotal <- quantidadeTotal + quantidade
               valorTotal <- valorTotal + (quantidade * 2.00)
               picoleValue <- quantidade * 2.00
               escreval("###############")
               Escreval("Quantidade de picolés de Tamarindo comprado(s): ", quantidade)
               escreval("Valor gasto com picolés de Tamarindo: R$", picoleValue)
            caso 6
               Escreval()
               escreval("Você escolheu sair!")
               fimalgoritmo
            outrocaso
               escreval("Número digitado incorreto. Tente novamente")
         fimescolha
      fimenquanto
   escreval()
   escreval("###############")
   Escreval("Quantidade de picolés comprados no total: ", quantidadeAtual)
   Escreval("Valor a ser pago no total: R$", valorAtual)
   escreval()
   escreval("Deseja seguir comprando? (S/N) ")
   leia(condicao)
      se ((condicao = "s") ou (condicao = "S")) entao
         condicao <- "s"
         condicao2 <- "s"
         number <- 0
         number2 <- 0
      fimse
   fimenquanto

   number2 <- 0
   enquanto (number2 <= 0) ou (number2 > 6) faca
      escreval()
      Escreval("#### CAIXA ####")
      Escreval("1 -- Á vista em dinheiro ou PIX (10% OFF)")
      Escreval("2 -- No cartão de débito (5% OFF)")
      Escreval("3 -- No cartão de crédito em 1x")
      Escreval("4 -- No cartão de crédito em 2x (+5% acréscimo)")
      Escreval("5 -- No cartão de crédito em 3x (+10% acréscimo)")
      Escreval("6 -- No cartão de crédito em 4x (+15% acréscimo)")
      Escreval("Digite o número correspondente á forma de pagamento: ")
      leia (number2)
      escolha(number2)
      caso 1
         desconto <- 10
         descontoTotal <- descontoTotal + 10
         valorFinalAtual <- valorAtual - (valorAtual * 0.10)
         valorFinal <- valorTotal - (valorTotal * 0.10)
      caso 2
         descontoTotal <- descontoTotal + 5
         desconto <- 5
         valorFinalAtual <- valorAtual - (valorAtual * 0.05)
         valorFinal <- valorTotal - (valorTotal * 0.05)
      caso 3
      caso 4
         parcelasTotal <- parcelasTotal + 2
         acrescimoTotal <- acrescimoTotal + 5
         parcelas <- 2
         acrescimo <- 5
         valorFinalAtual <- valorAtual + (valorAtual * 0.05)
         valorFinal <- valorTotal + (valorTotal * 0.05)
         valorParcelado <- valorFinal / parcelas
         valorParceladoTotal <- valorFinal / parcelasTotal
      caso 5
         parcelasTotal <- parcelasTotal + 3
         acrescimoTotal <- acrescimoTotal + 10
         parcelas <- 3
         acrescimo <- 10
         valorFinalAtual <- valorAtual + (valorAtual * 0.10)
         valorFinal <- valorTotal + (valorTotal * 0.10)
         valorParcelado <- valorFinal / parcelas
         valorParceladoTotal <- valorFinal / parcelasTotal
      caso 6
         parcelasTotal <- parcelasTotal + 4
         acrescimoTotal <- acrescimoTotal + 15
         parcelas <- 4
         acrescimo <- 15
         valorFinalAtual <- valorAtual + (valorAtual * 0.15)
         valorFinal <- valorTotal + (valorTotal * 0.15)
         valorParceladoTotal <- valorFinal / parcelasTotal
         valorParcelado <- valorFinal / parcelas
      outrocaso
         ESCREVAL("o número digitado é inválido! Tente novamente")
      fimescolha
   fimenquanto

   escreval()
   Escreval("#### RECIBO DA COMPRA ATUAL #####")
   Escreval("Quantidade de picolés comprados: ", quantidadeAtual)
   Escreval("Valor total: R$", valorAtual:2:1)
   Escreval("Desconto: ", desconto,"%")
   Escreval("Acréscimo: ", acrescimo,"%")
   Escreval("Número de parcelas: ", parcelas)
   Escreval("Valor por parcela: R$", valorParcelado)
   Escreval("Valor final pago: R$", valorFinalAtual:2:1)

   escreval()
   escreval("Deseja seguir comprando? (S/N) ")
   leia(condicao2)
   se ((condicao2 = "s") ou (condicao2 = "S")) entao
      condicao <- "s"
      condicao2 <- "s"
      number <- 0
      quantidadeAtual <- 0
      valorAtual <- 0
      number2 <- 0
   fimse
   fimenquanto

escreval()
Escreval("#### RECIBO DO TOTAL DE TODAS COMPRAS #####")
Escreval("Quantidade total de picolés comprados: ", quantidadeTotal)
Escreval("Valor total: R$", valorTotal:2:1)
Escreval("Desconto total: ", descontoTotal,"%")
Escreval("Acréscimo total: ", acrescimoTotal,"%")
Escreval("Número de parcelas total: ", parcelasTotal)
Escreval("Valor por parcela no total: R$", valorParceladoTotal)
Escreval("Valor final pago total: R$", valorFinal:2:1)
escreval()
escreval("Obrigado por comprar conosco!")

Fimalgoritmo