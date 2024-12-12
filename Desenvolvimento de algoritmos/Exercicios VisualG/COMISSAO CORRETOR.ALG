Algoritmo "Comissao Corretor"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/10/2024
Var
   // Seção de Declarações das variáveis
   nome : caractere
   valor, comissao : real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva("Digite seu nome: ")
   leia(nome)
   Escreva("Digite o valor do imóvel: ")
   leia(valor)

   se (valor >= 50000) entao
      comissao <- valor * (20/100)
   senao
      se (valor >= 30000)entao
         comissao <- valor * (15/100)
      senao
         comissao <- valor * (10/100)
      fimse
   fimse
   
   Escreval("Nome do corretor: ", nome)
   Escreval("Valor do imóvel: ", valor:2:2)
   Escreval("Comissão do corretor: ", comissao:2:2)

Fimalgoritmo