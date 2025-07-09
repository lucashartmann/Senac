Algoritmo "CONCESSIONARIA"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   :
// Autor(a)    : Lucas Hartmann
// Data atual  : 21/11/2024
Var
   // Seção de Declarações das variáveis


   faturamento: vetor[1..10] de real
   registroCarros: vetor [1..10] de inteiro
   i, numCadastro, quantCarros, numRegistro, number : inteiro
   comissao, valor, faturamentoTotal : real
   nome, condicao : caractere


Inicio
   number <- 0
   condicao <- "false"

   Escreval("### CONCESSIONÁRIA ###")
   escreval("## CADASTRO VENDEDOR ##")
   escreval()

   escreva("Digite seu nome: ")
   leia(nome)
   escreva("Digite seu número de cadastro: ")
   leia(numCadastro)

   enquanto (number < 1) ou (number > 4) faca
      escreval()
      escreval("## MENU ##")
      escreval("1 -- Cadastrar carro")
      escreval("2 -- Cadastrar venda")
      escreval("3 -- Ver faturamento mensal")
      escreval("4 -- Encerrar o programa")
      leia(number)
      escolha (number)
      caso 1
         escreval()
         escreva("Quantos carros você deseja cadastrar? ")
         leia(quantCarros)
         para i de 1 ate quantCarros faca
            escreva("Digite o número de registro do veiculo: ")
            leia(numRegistro)
            registroCarros[i] <- numRegistro
            escreval("Carro cadastrado com sucesso!")
         fimpara
      caso 2
         escreval()
         escreva("Quantos carros você deseja realizar a venda? ")
         leia(quantCarros)
         para i de 1 ate quantCarros faca
            escreva("Digite o número de registro do veiculo: ")
            leia(numRegistro)
            para i de 1 ate 10 faca
               se(registroCarros[i] = numRegistro) entao
                  escreval("Carro está registrado")
                  condicao <- "true"
               fimse
            fimpara
            se(condicao = "true") entao
               escreva("Digite o valor da venda: ")
               leia(valor)
               faturamento[i] <- valor
               escreval("Venda realizada!")
            senao
               escreval("Carro não cadastrado. Realize o cadastro primeiro")
            fimse
         fimpara
      caso 3
         escreval()
         para i de 1 ate 10 faca
            faturamentoTotal <- faturamentoTotal + faturamento[i]
         fimpara
         comissao <- faturamentoTotal * 0.15
         escreval("Voce escolheu ver o faturamento mensal")
         escreval("Faturamento mensal: ")
         para i de 1 ate 10 faca
            escreva(faturamento[i], "")
         fimpara
         escreval()
         escreval("Faturamento total: ", faturamentoTotal:2:2)
         escreval("Sua comissão no mês: ", comissao:2:2)
      caso 4
         escreval()
         escreval("Você escolheu encerrar o programa")
Fimalgoritmo
outrocaso
   escreval("O número digitado é inválido. Tente novamente")

fimescolha
number <- 0

fimenquanto

Fimalgoritmo