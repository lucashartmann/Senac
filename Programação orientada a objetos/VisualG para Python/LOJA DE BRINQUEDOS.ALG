Algoritmo "Loja de brinquedos"

// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   :
// Autor(a)    : Lucas
// Data atual  : 25/11/2024

Var

   number, parcelas, quantAtual, quantTotal, i, condicaoDois, j : inteiro
   valorProduto, valorFinal, valorParcelado, valorTotal, desconto, acrescimo  : real
   menu, menuPagamento, condicao, nome, pagamento : caractere
   valorAtual, valorFinalTotal : real
   valorProdutos : vetor[1..10] de real
   nomeProdutos : vetor[1..10] de caractere
   valorTotalProdutos : vetor[1..10] de real
   nomeTotalProdutos : vetor[1..10] de caractere
   meiosPagamento : vetor[1..10] de caractere
   quantProduto, l, m, quantPay : inteiro

funcao cadastroProduto(nome:caractere; valorProduto:real; i, j:inteiro) : inteiro
inicio
   valorProdutos[i] <- valorProduto
   nomeProdutos[i] <- nome
   valorTotalProdutos[j] <- valorProduto
   nomeTotalProdutos[j] <- nome
   retorne 1
fimfuncao
funcao cadastroPagamento(pagamento:caractere; i:inteiro) : inteiro
inicio
   meiosPagamento[i] <- pagamento
   retorne 1
fimfuncao

funcao menu : caractere
inicio
   number <- 0
   escreval()
   enquanto ((number < 1) ou (number > 7)) faca
      escreval("### MENU ###")
      escreval("1 -- Carrinho a controle remoto super máquina - R$ 500,00")
      escreval("2 -- Boneca Barbie - R$ 450,00")
      escreval("3 -- Boneco cobra comandos em ação - R$ 300,00")
      escreval("4 -- Boneco fofão - R$ 480,00")
      escreval("5 -- Vídeo game Atari - R$ 820,00")
      escreval("6 -- Jogo super mário - R$ 100,00")
      escreval("7 -- Bicicleta caloi cross extra - R$ 5.000,00")
      escreva("Digite o número correspondente á opção desejada: ")
      leia(number)
      escolha(number)
      caso 1
         valorProduto <- 500.00
         nome <- "Carrinho a controle remoto super máquina"
         escreva("Informe quantos você deseja comprar: ")
         leia(quantProduto)
         para l de 1 ate  quantProduto faca
            i <- i + 1
            j <- j + 1
            valorAtual <- valorAtual + valorProduto
            condicaoDois <- cadastroProduto(nome, valorProduto, i, j)
            se (condicaoDois = 1) entao
               escreval(Nome, " comprado!")
            senao
               escreval("Não foi possível finalizar a compra.")
            fimse
         fimpara
         quantAtual <- quantAtual + quantProduto
      caso 2
         valorProduto <- 450.00
         nome <- "Boneca Barbie"
         escreva("Informe quantos você deseja comprar: ")
         leia(quantProduto)
         para l de 1 ate  quantProduto faca
            i <- i + 1
            j <- j + 1
            valorAtual <- valorAtual + valorProduto
            condicaoDois <- cadastroProduto(nome, valorProduto, i, j)
            se (condicaoDois = 1) entao
               escreval(Nome, " comprado!")
            senao
               escreval("Não foi possível finalizar a compra.")
            fimse
         fimpara
         quantAtual <- quantAtual + quantProduto
      caso 3
         valorProduto <- 300.00
         nome <- "Boneco cobra comandos em ação"
         escreva("Informe quantos você deseja comprar: ")
         leia(quantProduto)
         para l de 1 ate  quantProduto faca
            i <- i + 1
            j <- j + 1
            valorAtual <- valorAtual + valorProduto
            condicaoDois <- cadastroProduto(nome, valorProduto, i, j)
            se (condicaoDois = 1) entao
               escreval(Nome, " comprado!")
            senao
               escreval("Não foi possível finalizar a compra.")
            fimse
         fimpara
         quantAtual <- quantAtual + quantProduto
      caso 4
         valorProduto <- 480.00
         nome <- "Boneco fofão"
         escreva("Informe quantos você deseja comprar: ")
         leia(quantProduto)
         para l de 1 ate  quantProduto faca
            i <- i + 1
            j <- j + 1
            valorAtual <- valorAtual + valorProduto
            condicaoDois <- cadastroProduto(nome, valorProduto, i, j)
            se (condicaoDois = 1) entao
               escreval(Nome, " comprado!")
            senao
               escreval("Não foi possível finalizar a compra.")
            fimse
         fimpara
         quantAtual <- quantAtual + quantProduto
      caso 5
         valorProduto <- 820.00
         nome <- "Vídeo game Atari"
         escreva("Informe quantos você deseja comprar: ")
         leia(quantProduto)
         para l de 1 ate  quantProduto faca
            i <- i + 1
            j <- j + 1
            valorAtual <- valorAtual + valorProduto
            condicaoDois <- cadastroProduto(nome, valorProduto, i, j)
            se (condicaoDois = 1) entao
               escreval(Nome, " comprado!")
            senao
               escreval("Não foi possível finalizar a compra.")
            fimse
         fimpara
         quantAtual <- quantAtual + quantProduto
      caso 6
         valorProduto <- 100.00
         nome <- "Jogo super mário"
         escreva("Informe quantos você deseja comprar: ")
         leia(quantProduto)
         para l de 1 ate  quantProduto faca
            i <- i + 1
            j <- j + 1
            valorAtual <- valorAtual + valorProduto
            condicaoDois <- cadastroProduto(nome, valorProduto, i, j)
            se (condicaoDois = 1) entao
               escreval(Nome, " comprado!")
            senao
               escreval("Não foi possível finalizar a compra.")
            fimse
         fimpara
         quantAtual <- quantAtual + quantProduto
      caso 7
         valorProduto <- 5000.00
         nome <- "Bicicleta caloi cross extra"
         escreva("Informe quantos você deseja comprar: ")
         leia(quantProduto)
         para l de 1 ate  quantProduto faca
            i <- i + 1
            j <- j + 1
            valorAtual <- valorAtual + valorProduto
            condicaoDois <- cadastroProduto(nome, valorProduto, i, j)
            se (condicaoDois = 1) entao
               escreval(Nome, " comprado!")
            senao
               escreval("Não foi possível finalizar a compra.")
            fimse
         fimpara
         quantAtual <- quantAtual + quantProduto
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
   escreval(dados)
fimfuncao

funcao menuPagamento : caractere
inicio
   pagamento <- "cartão de crédito em"
   escreval()
   enquanto ((number < 1) ou (number > 7)) faca
      escreval("### MENU DE PAGAMENTO ###")
      escreval("1 - A vista em dinheiro ou PIX, 5% de desconto")
      escreval("2 - No cartão de débito")
      escreval("3 - No cartão de crédito em 1x, acréscimo de 5%")
      escreval("4 - No cartão de crédito em 2x, acréscimo de 5%")
      escreval("5 - No cartão de crédito em 3x, acréscimo de 8%")
      escreval("6 - No cartão de crédito em 4x, acréscimo de 8%")
      escreval("7 - No cartão de crédito em 5x, acréscimo de 10%")
      escreva("Digite o número correspondente á opção: ")
      leia(number)
      escolha(number)
      caso 1
         pagamento <- "a vista"
         desconto <- 5
         valorFinal <- valorAtual - (valorAtual * (desconto / 100))
         valorFinalTotal <- valorFinalTotal + valorFinal
         m <- m + 1
         condicaoDois <- cadastroPagamento(pagamento, m)
         quantPay <- quantPay + 1
      caso 2
         pagamento <- "cartão de débito"
         valorFinal <- valorAtual
         valorFinalTotal <- valorFinalTotal + valorFinal
         m <- m + 1
         condicaoDois <- cadastroPagamento(pagamento, m)
         quantPay <- quantPay + 1
      caso 3
         pagamento <- pagamento + " 1x"
         acrescimo <- 5
         valorFinal <- valorAtual + (valorAtual * (acrescimo / 100))
         parcelas <- 1
         valorParcelado <- valorfinal / parcelas
         valorFinalTotal <- valorFinalTotal + valorFinal
         m <- m + 1
         condicaoDois <- cadastroPagamento(pagamento, m)
         quantPay <- quantPay + 1
      caso 4
         pagamento <- pagamento + " 2x"
         acrescimo <- 5
         valorFinal <- valorAtual + (valorAtual * (acrescimo / 100))
         parcelas <- 2
         valorParcelado <- valorfinal / parcelas
         valorFinalTotal <- valorFinalTotal + valorFinal
         m <- m + 1
         condicaoDois <- cadastroPagamento(pagamento, m)
         quantPay <- quantPay + 1
      caso 5
         pagamento <- pagamento + " 3x"
         acrescimo <- 8
         valorFinal <- valorAtual + (valorAtual * (acrescimo / 100))
         parcelas <- 3
         valorParcelado <- valorfinal / parcelas
         valorFinalTotal <- valorFinalTotal + valorFinal
         m <- m + 1
         condicaoDois <- cadastroPagamento(pagamento, m)
         quantPay <- quantPay + 1
      caso 6
         pagamento <- pagamento + " 4x"
         acrescimo <- 8
         valorFinal <- valorAtual + (valorAtual * (acrescimo / 100))
         parcelas <- 4
         valorParcelado <- valorfinal / parcelas
         valorFinalTotal <- valorFinalTotal + valorFinal
         m <- m + 1
         condicaoDois <- cadastroPagamento(pagamento, m)
         quantPay <- quantPay + 1
      caso 7
         pagamento <- pagamento + " 5x"
         acrescimo <- 10
         valorFinal <- valorAtual + (valorAtual * (acrescimo / 100))
         parcelas <- 5
         valorParcelado <- valorfinal / parcelas
         valorFinalTotal <- valorFinalTotal + valorFinal
         m <- m + 1
         condicaoDois <- cadastroPagamento(pagamento, m)
         quantPay <- quantPay + 1
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
   escreval(dadosPagamento)
   quantAtual <- 0
   valorAtual <- 0
   i <- 0
   desconto <- 0
   acrescimo <- 0
   parcelas <- 0
fimfuncao

funcao dados : caractere
inicio
   escreval()
   escreval("Quantidade de produtos comprados na compra atual: ", quantAtual)

   escreval("-----------")
   escreval("Produtos comprados: ")
   para i de 1 ate quantAtual faca
      escreval("Nome: ", nomeProdutos[i])
      escreval("Preço: R$", valorProdutos[i]:2:2)
   fimpara
   escreval("-----------")
   escreval("Valor da compra atual: R$", valorAtual:2:2)
fimfuncao

funcao dadosPagamento : caractere
inicio
   escreval()
   escreval("#### DADOS DE PAGAMENTO ####")
   escreval(dados)
   escreval("Método de pagamento: ", pagamento)
   se (desconto > 0) entao
      escreval("Desconto: %",desconto)
   fimse
   se(acrescimo > 0) entao
      escreval("Acréscimo: %",acrescimo)
   fimse
   escreval("Valor Final: R$", valorFinal:2:2)
   se(parcelas > 0) entao
      escreval ("Número de parcelas: ", parcelas)
      escreval("Valor das parcelas: R$", valorParcelado:2:2)
   fimse
fimfuncao


Inicio
   condicao <- "s"
   quantTotal <- 0
   valorTotal <- 0
   escreval("#### LOJA DE BRINQUEDOS ####")
   enquanto ((condicao = "s") ou (condicao = "S")) faca
      enquanto ((condicao = "s") ou (condicao = "S")) faca
         escreval(menu)
         escreval()
         escreval("Deseja comprar mais? (S/N)")
         leia(condicao)
         number <- 0
      fimenquanto
      valorTotal <- valorTotal + valorAtual
      quantTotal <- quantTotal + quantAtual
      escreval(menuPagamento)
      escreval()
      escreval("Deseja comprar mais? (S/N)")
      leia(condicao)
      number <- 0
   fimenquanto
   escreval()
   escreval("################")

   escreval("-----------")
   escreval("Produtos comprados no dia: ")
   para i de 1 ate quantTotal faca
      escreval("Nome: ", nomeTotalProdutos[i])
      escreval("Preço: R$", valorTotalProdutos[i]:2:2)
   fimpara
   escreval("-----------")
   escreval("Quantidade total de produtos comprados no dia: ", quantTotal)
   escreval("Valor total das compras no dia: R$", valorTotal:2:2)
   escreval("Valor total final das compras no dia: R$", valorFinalTotal:2:2)

   escreval("-----------")
   escreval("Meios de pagamento usados no dia: ")
   para i de 1 ate quantPay faca
      escreval(meiosPagamento[i])
   fimpara
   escreval("-----------")
   escreval("Obrigado por comprar conosco!")

Fimalgoritmo