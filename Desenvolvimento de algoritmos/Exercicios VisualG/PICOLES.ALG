Algoritmo "Picoles"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/10/2024
Var
   quantidade, number : inteiro
   value, menuValue : real


Inicio
   Escreva("## VENDA DE PICOLÉS ##")
   menuValue <- 0
   enquanto menuValue = 0 faca
      Escreva("## MENU ##")
      Escreval("Digite o número correspondente ao picolé que você deseja: ")
      Escreval("1 -- Picolé de Uva (R$1,00)")
      Escreval("2 -- Picolé de Laranja (R$1,25)")
      Escreval("3 -- Picolé de Milho (R$1,50)")
      Escreval("4 -- Picolé de Coco queimado (R$1,80)")
      Escreval("5 -- Picolé de Tamarindo (R$2,00)")
      Escreval("6 -- Sair do menu")
      leia (number)
      se(number = 6) entao
         Escreval("Você escolheu sair!")
         menuValue <- 1
      senao
         se(number = 1) entao
            quantidade <- quantidade + 1
            value <- value + 1.00
            Escreval("Picolé de Uva comprado!")
         senao
            se(number = 2) entao
               quantidade <- quantidade + 1
               value <- value + 1.25
               Escreval("Picolé de Laranja comprado!")
            senao
               se(number = 3) entao
                  quantidade <- quantidade + 1
                  value <- value + 1.50
                  Escreval("Picolé de Milho comprado!")
               senao
                  se(number = 4) entao
                     quantidade <- quantidade + 1
                     value <- value + 1.80
                     Escreval("Picolé de Coco queimado comprado!")
                  senao
                     se(number = 5) entao
                        quantidade <- quantidade + 1
                        value <- value + 2.00
                        Escreval("Picolé de Tamarindo comprado!")
                     senao
                        escreval("o número digitado é inválido!")
                     fimse
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimenquanto
   escreval()
   Escreval("## RESULTADO COMPRA ##")
   Escreval("Quantidade de picolés comprados: ", quantidade)
   Escreval("Valor a ser pago: ", value)


   Escreva("## VENDA DE PICOLÉS ##")
   menuValue <- 0
   enquanto menuValue = 0 faca
      Escreva("## MENU ##")
      Escreval("Digite o número correspondente ao picolé que você deseja: ")
      Escreval("1 -- Picolé de Uva (R$1,00)")
      Escreval("2 -- Picolé de Laranja (R$1,25)")
      Escreval("3 -- Picolé de Milho (R$1,50)")
      Escreval("4 -- Picolé de Coco queimado (R$1,80)")
      Escreval("5 -- Picolé de Tamarindo (R$2,00)")
      Escreval("6 -- Sair do menu")
      leia (number)
      escolha(number)
      Caso 1
         quantidade <- quantidade + 1
         value <- value + 1.00
         Escreval("Picolé de Uva comprado!")
      Caso 2
         quantidade <- quantidade + 1
         value <- value + 1.25
         Escreval("Picolé de Laranja comprado!")
      Caso 3
         quantidade <- quantidade + 1
         value <- value + 1.50
         Escreval("Picolé de Milho comprado!")
      Caso 4
         quantidade <- quantidade + 1
         value <- value + 1.80
         Escreval("Picolé de Coco comprado!")
      Caso 5
         quantidade <- quantidade + 1
         value <- value + 2.00
         Escreval("Picolé de Tamarindo comprado!")
      Caso 6
         Escreval("Você escolheu sair!")
         menuValue <- 1
      OUTROCASO
         ESCREVA("o número digitado é inválido!")
      fimescolha
   fimenquanto

   escreval()
   Escreval("## RESULTADO COMPRA ##")
   Escreval("Quantidade de picolés comprados: ", quantidade)
   Escreval("Valor a ser pago: ", value)



Fimalgoritmo