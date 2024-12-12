Algoritmo "CORRETORA"

// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Lucas Augusto Hartmann
// Data atual  : 14/11/2024

Var
   nome : caractere
   v, v1, v2, v3, v4, v5, mediaVendedor, faturamentoVendedor : real
   faturamentoCorretora, mediaCorretora, valor : real
   i, quantCorretora, quantVendedor, number : inteiro

Inicio
   number <- 0
   escreval("#### CORRETORA  #####")
   para  i de 1 ate 2 faca
      quantVendedor <- 0
      escreval()
      escreva("Digite o nome do vendedor: ")
      leia(nome)
      number <- 0
      enquanto (number < 1) ou (number > 7) faca
         escreval("------------- MENU ------------")
         escreval("1 -- Cadastrar venda de janeiro: ")
         escreval("2 -- Cadastrar venda de fevereiro: ")
         escreval("3 -- Cadastrar venda de março: ")
         escreval("4 -- Cadastrar venda de abril: ")
         escreval("5 -- Cadastrar venda de maio: ")
         escreval("6 -- Cadastrar venda de junho: ")
         escreval("7 -- Sair do menu")
         escreval("Digite o número correspondente á opção desejada: ")
         leia(number)
         escolha(number)
            escreval()
         caso 1
            escreval("Você entrou em cadastrar venda de janeiro")
            escreva("Digite quantas vendas voc? deseja cadastrar: ")
            leia(quant)
            para i de 1 ate quant faca
               escreval("Digite o valor da venda: ")
               leia(valor)
               v <- v + valor
               quantCorretora <- quantCorretora + 1
               quantVendedor <- quantVendedor + 1
            fimpara
            number <- 0
         caso 2
            escreval("Você entrou em cadastrar venda de fevereiro")
            escreva("Digite quantas vendas voc? deseja cadastrar: ")
            leia(quant)
            para i de 1 ate quant faca
               escreval("Digite o valor da venda: ")
               leia(valor)
               v1 <- v1 + valor
               quantCorretora <- quantCorretora + 1
               quantVendedor <- quantVendedor + 1
               number <- 0
            caso 3
               escreval("Você entrou em cadastrar venda de março")
               escreva("Digite quantas vendas voc? deseja cadastrar: ")
               leia(quant)
               para i de 1 ate quant faca
                  escreval("Digite o valor da venda: ")
                  leia(valor)
                  v2 <- v2 + valor
                  quantCorretora <- quantCorretora + 1
                  quantVendedor <- quantVendedor + 1
               fimpara
               number <- 0
            caso 4
               escreval("Você entrou em cadastrar venda de abril")
               escreva("Digite quantas vendas voc? deseja cadastrar: ")
               leia(quant)
               para i de 1 ate quant faca
                  escreval("Digite o valor da venda: ")
                  leia(valor)
                  v3 <- v3 + valor
                  quantCorretora <- quantCorretora + 1
                  quantVendedor <- quantVendedor + 1
               fimpara
               number <- 0
            caso 5
               escreval("Você entrou em cadastrar venda de maio")
               escreva("Digite quantas vendas voc? deseja cadastrar: ")
               leia(quant)
               para i de 1 ate quant faca
                  escreval("Digite o valor da venda: ")
                  leia(valor)
                  v4 <- v4 + valor
                  quantCorretora <- quantCorretora + 1
                  quantVendedor <- quantVendedor + 1
               fimpara
               number <- 0
            caso 6
               escreval("Você entrou em cadastrar venda de junho")
               escreva("Digite quantas vendas voc? deseja cadastrar: ")
               leia(quant)
               para i de 1 ate quant faca
                  escreval("Digite o valor da venda: ")
                  leia(valor)
                  v5 <- v5 + valor
                  quantCorretora <- quantCorretora + 1
                  quantVendedor <- quantVendedor + 1
               fimpara
               number <- 0
            caso 7
            outrocaso
               escreval("O número digitado é inválido. Tente novamente")
            fimescolha
         fimenquanto

         faturamentoVendedor <- (v + v1 + v2 + v3 + v4 + v5)
         mediaVendedor <- (faturamentoVendedor / 6 )
         faturamentoCorretora <- faturamentoCorretora + faturamentoVendedor

         escreval()
         escreval("##### DADOS DO VENDEDOR #####")
         escreval("Nome do vendedor: ", nome)
         escreval("Valor das vendas mensais (em ordem): ", v, ", ", v1, ", ", v2, ", ", v3, ", ", v4, ", ", v5)
         escreval("Quantidade de vendas no semestre: ", quantVendedor)
         escreval("Faturamento semestral: R$", faturamentoVendedor:2:1)
         escreval("Média do faturamento semestral: R$", mediaVendedor:2:1)
      fimpara

      mediaCorretora <- (faturamentoCorretora / 6)

      escreval()
      escreval("#### DADOS DA CORRETORA ####")
      escreval("Quantidade de vendas: ", quantCorretora)
      escreval("Faturamento semestral: R$", faturamentoCorretora:2:1)
      escreval("Média do semestre: R$", mediaCorretora:2:1)


Fimalgoritmo