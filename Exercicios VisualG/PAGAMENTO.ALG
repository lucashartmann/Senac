Algoritmo "pagamento"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 04/11/2024
Var
   // Seção de Declarações das variáveis
   nome : caractere
   valorInicial, valorTotal, : real
   opcao,desconto, acrescimo : inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva("Digite seu nome: ")
   leia(nome)
   Escreva("Digite o valor da venda: ")
   leia(valorInicial)
   Escreval("## MENU PAGAMENTO ##")
   Escreval("Digite o número da operação desejada: ")
   Escreval("1 -- Venda a vista (10% de desconto)")
   Escreval("2 -- Venda a prazo de 30 dias (5% de desconto)")
   Escreval("3 -- Venda a prazo de 60 dias")
   Escreval("4 -- Venda a prazo de 90 dias (5% de acréscimo)")
   Escreval("5 -- Venda com cartão de débito (8% de desconto)")
   Escreval("6 -- Venda com cartão de crédito (7% de desconto)")
   leia(opcao)
   escolha(opcao)
   caso 1
      desconto <- 10
      valorTotal <- valorInicial - (valorInicial * (desconto/100))
   caso 2
      desconto <- 5
      valorTotal <- valorInicial - (valorInicial * (desconto/100))
   caso 3
      valorTotal <- valorInicial
   caso 4
      acrescimo <- 5
      valorTotal <- valorInicial + (valorInicial * (acrescimo/100))
   caso 5
      desconto <- 8
      valorTotal <- valorInicial - (valorInicial * (desconto/100))
   caso 6
      desconto <- 7
      valorTotal <- valorInicial - (valorInicial * (desconto/100))
   fimescolha

   se (opcao < 7) e (opcao > 0) entao
      Escreval("Nome do vendedor: ", nome)
      Escreval("Valor da venda: ", valorInicial:2:1)
      Escreval("Valor total da venda: ", valorTotal:2:1)
   senao
      escreval("Número digitado inválido. Tente novamente")
   fimse

Fimalgoritmo