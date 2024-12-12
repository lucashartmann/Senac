Algoritmo "corretor com switch"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Lucas
// Data atual  : 07/11/2024
Var
   nome, condicao : caractere
   valor, comissao : real

Inicio
   condicao <- "s"
   
   enquanto ((condicao = "S") ou (condicao = "s")) faca
   
      escreval("## CORRETAGEM ##")
      escreva("Informe o nome:")
      leia(nome)
      escreva("Informe o valor: ")
      leia(valor)
      
      se(valor >= 50000) entao
         comissao <- valor * 0.20
      senao
         se (valor >= 30000) e (valor < 50000) entao
            comissao <- valor * 0.15
         senao
            comissao <- valor * 0.10
         fimse
      fimse
      
      escreval()
      
      escreval("## RESULTADO DA CONSULTA ##")
      escreval("Nome do corretor: ", nome)
      escreval("Valor do imóvel: ", valor)
      escreval("Comissão: ", comissao)

      escreval("Deseja fazer o cadastro novamente? (S/N)")
      leia(condicao)
      
   fimenquanto

Fimalgoritmo