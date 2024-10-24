Algoritmo "juros"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/10/2024
Var
   prestacao, juros : real
   dias : inteiro

Inicio
   escreval("## SISTEMA DE COBRANÇA DE JUROS")
   
   escreva("Informe sua prestação: ")
   leia (prestacao)
   escreva("Informe os dias de atraso: ")
   leia (dias)
   escreva("Informe a taxa de juros: ")
   leia (juros)
   
   escreval
   
   escreval("## RESULTADO DA CONSULTA")
   escreval("Valor da prestação: R$",prestacao:2:2)
   escreval("Dias em atraso: ", dias)
   escreval("Juros: %", juros)
   juros <- (juros * dias) / 30
   escreval("Valor do juros: R$", juros:2:2)
   prestacao <- prestacao + juros
   escreva("Valor final para pagar: R$", prestacao:2:2)

Fimalgoritmo