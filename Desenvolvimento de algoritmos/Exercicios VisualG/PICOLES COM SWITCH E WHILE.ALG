Algoritmo "Picoles com switch e while"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/10/2024
Var
   quantidade, quantidadeTotal, number, number2, desconto, parcelas, acrescimo : inteiro
   valorTotal, picoleValue, valorFinal: real
   condicao : caractere

Inicio
   condicao <- "s"
   Escreval("#### VENDA DE PICOL�S ####")
   enquanto ((condicao = "s") ou (condicao = "S")) faca
      Escreval("#### MENU ####")
      Escreval("1 -- Picol� de Uva (R$1,00)")
      Escreval("2 -- Picol� de Laranja (R$1,25)")
      Escreval("3 -- Picol� de Milho (R$1,50)")
      Escreval("4 -- Picol� de Coco queimado (R$1,80)")
      Escreval("5 -- Picol� de Tamarindo (R$2,00)")
      Escreval("Digite o n�mero correspondente ao picol� que voc� deseja: ")
      leia (number)
      //enquanto (number < 0) ou (number > 5) faca
      //   escreval("N�mero digitado incorreto. Tente novamente")
      //   Escreval("Digite o n�mero correspondente ao picol� que voc� deseja: ")
      //   leia (number)
      //fimenquanto
      escolha(number)
      Caso 1
         Escreval("Quantos picol�s deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.00)
         picoleValue <- quantidade * 1.00
         escreval("###############")
         Escreval("Quantidade de picol�s de Uva comprado(s): ", quantidade)
         escreval("Valor gasto com picol�s de Uva: R$", picoleValue)
      Caso 2
         Escreval("Quantos picol�s deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.25)
         picoleValue <- quantidade * 1.25
         escreval("###############")
         Escreval("Quantidade de picol�s de Laranja comprado(s): ", quantidade)
         escreval("Valor gasto com picol�s de Laranja: R$", picoleValue)
      Caso 3
         Escreval("Quantos picol�s deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.50)
         picoleValue <- quantidade * 1.50
         escreval("###############")
         Escreval("Quantidade de picol�s de Milho comprado(s): ", quantidade)
         escreval("Valor gasto com picol�s de Milho: R$", picoleValue)
      Caso 4
         Escreval("Quantos picol�s deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 1.80)
         picoleValue <- quantidade * 1.80
         escreval("###############")
         Escreval("Quantidade de picol�s de Coco queimado comprado(s): ", quantidade)
         escreval("Valor gasto com picol�s de Coco queimado: R$", picoleValue)
      Caso 5
         Escreval("Quantos picol�s deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         valorTotal <- valorTotal + (quantidade * 2.00)
         picoleValue <- quantidade * 2.00
         escreval("###############")
         Escreval("Quantidade de picol�s de Tamarindo comprado(s): ", quantidade)
         escreval("Valor gasto com picol�s de Tamarindo: R$", picoleValue)
      outrocaso
         escreval("numero digitado incorreto. Tente novamente")
      fimescolha

      escreval()
      escreval("###############")
      Escreval("Quantidade de picol�s comprados no total: ", quantidadeTotal)
      Escreval("Valor a ser pago no total: R$", valorTotal)
      escreval()
      escreval("Deseja seguir comprando? (S/N) ")
      leia(condicao)
   fimenquanto

   number2 <- 1
   enquanto (number2 < 0) ou (number2 > 6) faca
      Escreval("#### CAIXA ####")
      Escreval("1 -- A vista em dinheiro ou PIX (10% OFF)")
      Escreval("2 -- No cartao de d�bito (5% OFF)")
      Escreval("3 -- No cartao de credito em 1x")
      Escreval("4 -- No cartao de credito em 2x (+5% acr�scimo)")
      Escreval("5 -- No cartao de credito em 3x (+10% acr�scimo)")
      Escreval("6 -- No cartao de credito em 4x (+15% acr�scimo)")
      Escreval("Digite o n�mero correspondente � forma de pagamento: ")
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
      ESCREVA("o n�mero digitado � inv�lido! Tente novamente")
   fimescolha

   escreval()
   Escreval("#### RECIBO #####")
   Escreval("Quantidade de picol�s comprados: ", quantidadeTotal)
   Escreval("Valor total: R$", valorTotal)
   Escreval("Desconto: ", desconto)
   Escreval("Acr�scimo: ", acrescimo)
   Escreval("N�mero de parcelas: ", parcelas)
   Escreval("Valor final pago: R$", valorTotal)

Fimalgoritmo