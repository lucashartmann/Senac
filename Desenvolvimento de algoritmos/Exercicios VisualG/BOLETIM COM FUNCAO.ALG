Algoritmo "Boletim com Funcao"
//
//
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/11/2024
Var
   // Seção de Declarações das variáveis
   resultado : real
   n, n1, n2, n3 : real

funcao Media(n, n1, n2, n3 : real) : real
var
   total : real

inicio
   total <- (n + n1 + n2 + n3) / 4
   se total >= 7 entao
      escreval("APROVADO")
   senao
      se total >= 5 entao
         escreval("RECUPERAÇÃO")
      senao
         escreval("REPROVADO")
      fimse
   fimse
   retorne total
fimfuncao

Inicio
   escreval("#####BOLETIM#####")
   escreva("Informe sua primeira nota: ")
   leia(n)
   escreva("Informe sua primeira nota: ")
   leia(n1)
   escreva("Informe sua primeira nota: ")
   leia(n2)
   escreva("Informe sua primeira nota: ")
   leia(n3)
   escreval()
   escreval("####RESULTADOS####")
   escreval("Notas em ordem: ", n, ", ", n1, ", ", n2, ", ", n3)
   escreva("Situação curricular: ")
   resultado <- Media(n, n1, n2, n3)
   escreval("Média: ", resultado)
Fimalgoritmo