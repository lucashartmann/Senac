Algoritmo "Picoles"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/10/2024
Var
   quantidade, number : inteiro
   value, menuValue : real


Inicio
   Escreva("## VENDA DE PICOL�S ##")
   menuValue <- 0
   enquanto menuValue = 0 faca
      Escreva("## MENU ##")
      Escreval("Digite o n�mero correspondente ao picol� que voc� deseja: ")
      Escreval("1 -- Picol� de Uva (R$1,00)")
      Escreval("2 -- Picol� de Laranja (R$1,25)")
      Escreval("3 -- Picol� de Milho (R$1,50)")
      Escreval("4 -- Picol� de Coco queimado (R$1,80)")
      Escreval("5 -- Picol� de Tamarindo (R$2,00)")
      Escreval("6 -- Sair do menu")
      leia (number)
      se(number = 6) entao
         Escreval("Voc� escolheu sair!")
         menuValue <- 1
      senao
         se(number = 1) entao
            quantidade <- quantidade + 1
            value <- value + 1.00
            Escreval("Picol� de Uva comprado!")
         senao
            se(number = 2) entao
               quantidade <- quantidade + 1
               value <- value + 1.25
               Escreval("Picol� de Laranja comprado!")
            senao
               se(number = 3) entao
                  quantidade <- quantidade + 1
                  value <- value + 1.50
                  Escreval("Picol� de Milho comprado!")
               senao
                  se(number = 4) entao
                     quantidade <- quantidade + 1
                     value <- value + 1.80
                     Escreval("Picol� de Coco queimado comprado!")
                  senao
                     se(number = 5) entao
                        quantidade <- quantidade + 1
                        value <- value + 2.00
                        Escreval("Picol� de Tamarindo comprado!")
                     senao
                        escreval("o n�mero digitado � inv�lido!")
                     fimse
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimenquanto
   escreval()
   Escreval("## RESULTADO COMPRA ##")
   Escreval("Quantidade de picol�s comprados: ", quantidade)
   Escreval("Valor a ser pago: ", value)


   Escreva("## VENDA DE PICOL�S ##")
   menuValue <- 0
   enquanto menuValue = 0 faca
      Escreva("## MENU ##")
      Escreval("Digite o n�mero correspondente ao picol� que voc� deseja: ")
      Escreval("1 -- Picol� de Uva (R$1,00)")
      Escreval("2 -- Picol� de Laranja (R$1,25)")
      Escreval("3 -- Picol� de Milho (R$1,50)")
      Escreval("4 -- Picol� de Coco queimado (R$1,80)")
      Escreval("5 -- Picol� de Tamarindo (R$2,00)")
      Escreval("6 -- Sair do menu")
      leia (number)
      escolha(number)
      Caso 1
         quantidade <- quantidade + 1
         value <- value + 1.00
         Escreval("Picol� de Uva comprado!")
      Caso 2
         quantidade <- quantidade + 1
         value <- value + 1.25
         Escreval("Picol� de Laranja comprado!")
      Caso 3
         quantidade <- quantidade + 1
         value <- value + 1.50
         Escreval("Picol� de Milho comprado!")
      Caso 4
         quantidade <- quantidade + 1
         value <- value + 1.80
         Escreval("Picol� de Coco comprado!")
      Caso 5
         quantidade <- quantidade + 1
         value <- value + 2.00
         Escreval("Picol� de Tamarindo comprado!")
      Caso 6
         Escreval("Voc� escolheu sair!")
         menuValue <- 1
      OUTROCASO
         ESCREVA("o n�mero digitado � inv�lido!")
      fimescolha
   fimenquanto

   escreval()
   Escreval("## RESULTADO COMPRA ##")
   Escreval("Quantidade de picol�s comprados: ", quantidade)
   Escreval("Valor a ser pago: ", value)



Fimalgoritmo