Algoritmo "CONCESSIONARIA"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Miguel
// Descri��o   :
// Autor(a)    : Lucas Hartmann
// Data atual  : 21/11/2024
Var
   // Se��o de Declara��es das vari�veis


   faturamento: vetor[1..10] de real
   registroCarros: vetor [1..10] de inteiro
   i, numCadastro, quantCarros, numRegistro, number : inteiro
   comissao, valor, faturamentoTotal : real
   nome, condicao : caractere


Inicio
   number <- 0
   condicao <- "false"

   Escreval("### CONCESSION�RIA ###")
   escreval("## CADASTRO VENDEDOR ##")
   escreval()

   escreva("Digite seu nome: ")
   leia(nome)
   escreva("Digite seu n�mero de cadastro: ")
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
         escreva("Quantos carros voc� deseja cadastrar? ")
         leia(quantCarros)
         para i de 1 ate quantCarros faca
            escreva("Digite o n�mero de registro do veiculo: ")
            leia(numRegistro)
            registroCarros[i] <- numRegistro
            escreval("Carro cadastrado com sucesso!")
         fimpara
      caso 2
         escreval()
         escreva("Quantos carros voc� deseja realizar a venda? ")
         leia(quantCarros)
         para i de 1 ate quantCarros faca
            escreva("Digite o n�mero de registro do veiculo: ")
            leia(numRegistro)
            para i de 1 ate 10 faca
               se(registroCarros[i] = numRegistro) entao
                  escreval("Carro est� registrado")
                  condicao <- "true"
               fimse
            fimpara
            se(condicao = "true") entao
               escreva("Digite o valor da venda: ")
               leia(valor)
               faturamento[i] <- valor
               escreval("Venda realizada!")
            senao
               escreval("Carro n�o cadastrado. Realize o cadastro primeiro")
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
         escreval("Sua comiss�o no m�s: ", comissao:2:2)
      caso 4
         escreval()
         escreval("Voc� escolheu encerrar o programa")
Fimalgoritmo
outrocaso
   escreval("O n�mero digitado � inv�lido. Tente novamente")

fimescolha
number <- 0

fimenquanto

Fimalgoritmo