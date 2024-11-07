Algoritmo "Picoles com switch e while"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/10/2024
Var
   quantidade, quantidadeTotal, number : inteiro
   value, picoleValue: real
   condicao : caractere

Inicio
   condicao <- "s"
   Escreval("## VENDA DE PICOLÉS ##")
   enquanto ((condicao = "s") ou (condicao = "S")) faca
      Escreval("## MENU ##")
      Escreval("1 -- Picolé de Uva (R$1,00)")
      Escreval("2 -- Picolé de Laranja (R$1,25)")
      Escreval("3 -- Picolé de Milho (R$1,50)")
      Escreval("4 -- Picolé de Coco queimado (R$1,80)")
      Escreval("5 -- Picolé de Tamarindo (R$2,00)")
      Escreval("Digite o número correspondente ao picolé que você deseja: ")
      leia (number)
      escolha(number)
      Caso 1
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         value <- value + (quantidade * 1.00)
         picoleValue <- quantidade * 1.00
         Escreval("Quantidade de picolés de Uva comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Uva: R$", picoleValue)
      Caso 2
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         value <- value + (quantidade * 1.25)
         picoleValue <- quantidade * 1.25
         Escreval("Quantidade de picolés de Laranja comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Laranja: R$", picoleValue)
      Caso 3
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         value <- value + (quantidade * 1.50)
         picoleValue <- quantidade * 1.50
         Escreval("Quantidade de picolés de Milho comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Milho: R$", picoleValue)
      Caso 4
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         value <- value + (quantidade * 1.80)
         picoleValue <- quantidade * 1.80
         Escreval("Quantidade de picolés de Coco queimado comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Coco queimado: R$", picoleValue)
      Caso 5
         Escreval("Quantos picolés deseja comprar?")
         leia(quantidade)
         quantidadeTotal <- quantidadeTotal + quantidade
         value <- value + (quantidade * 2.00)
         picoleValue <- quantidade * 2.00
         Escreval("Quantidade de picolés de Tamarindo comprado(s): ", quantidade)
         escreval("Valor gasto com picolés de Tamarindo: R$", picoleValue)
      OUTROCASO
         ESCREVA("o número digitado é inválido! Tente novamente")
      fimescolha

      escreval()
      Escreval("Quantidade de picolés comprados no total: ", quantidadeTotal)
      Escreval("Valor a ser pago no total: R$", value)
      escreval("Deseja seguir comprando? (S/N) ")
      leia(condicao)

   fimenquanto
   escreval()
   Escreval("## RESULTADO COMPRA ##")
   Escreval("Quantidade de picolés comprados: ", quantidade)
   Escreval("Valor a ser pago: R$", value)

Fimalgoritmo