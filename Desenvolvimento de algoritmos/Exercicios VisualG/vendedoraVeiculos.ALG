Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/10/2024
Var
   preco_fabrica, percent_revendedor, imposto, preco_final : real
   nome: caractere

Inicio
   Escreval("## LOJA DE VEICULOS MARCELÃO")
   Escreval("Informe o nome do veiculo")
   leia (nome)
   Escreval("Informe o preço do veiculo na fabrica")
   leia (preco_fabrica)
   imposto <- 45 / 100
   percent_revendedor <- 28 / 100
   percent_revendedor <- preco_fabrica * percent_revendedor
   imposto <- preco_fabrica * imposto
   preco_final <- preco_fabrica + percent_revendedor + imposto
   Escreval("Nome do veículo: ", nome)
   Escreval("Preço de fábrica do veículo: ", preco_fabrica:2:2)
   Escreval("Percentual do vendedor: ", percent_revendedor:2:2)
   Escreval("Imposto: ", imposto:2:2)
   Escreval("Preço final do veículo para revenda: ", preco_final:2:2)

Fimalgoritmo