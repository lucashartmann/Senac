Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/10/2024
Var
   preco_fabrica, percent_revendedor, imposto, preco_final : real
   nome: caractere

Inicio
   Escreval("## LOJA DE VEICULOS MARCEL�O")
   Escreval("Informe o nome do veiculo")
   leia (nome)
   Escreval("Informe o pre�o do veiculo na fabrica")
   leia (preco_fabrica)
   imposto <- 45 / 100
   percent_revendedor <- 28 / 100
   percent_revendedor <- preco_fabrica * percent_revendedor
   imposto <- preco_fabrica * imposto
   preco_final <- preco_fabrica + percent_revendedor + imposto
   Escreval("Nome do ve�culo: ", nome)
   Escreval("Pre�o de f�brica do ve�culo: ", preco_fabrica:2:2)
   Escreval("Percentual do vendedor: ", percent_revendedor:2:2)
   Escreval("Imposto: ", imposto:2:2)
   Escreval("Pre�o final do ve�culo para revenda: ", preco_final:2:2)

Fimalgoritmo