Algoritmo "folha salarial"

// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Miguel
// Descrição   :
// Autor(a)    : Lucas Hartmann
// Data atual  : 27/11/2024

Var

   name: caractere
   quantHours, quantEmployee, number, i: inteiro
   salaryPerHour, foodSalary, transportSalary, liquidSalary, salary : real
   inssDescountPercent, inssDescount, transportDescount, foodDescount: real

funcao cadastro() : caractere
inicio
   escreval()
   escreval("---- Entrada de dados ----")
   escreva("Digite o nome do funcionario: ")
   leia(name)
   escreva("Digite a quantidade de horas trabalhadas no mês: ")
   leia(quantHours)
   escreva("Digite o sálario por hora: ")
   leia(salaryPerHour)
   escreva("Digite o valor do vale de alimentação: ")
   leia(foodSalary)
   escreva("Digite o valor do vale transporte: ")
   leia(transportSalary)
   number <- getSalary
fimfuncao


funcao getSalary() : inteiro
inicio
   salary <- salaryPerHour * quantHours
   se (salary <= 1412.00) entao
      inssDescountPercent <- 7.5
   senao
      se (salary <= 2666.68) entao
         inssDescountPercent <- 9
      senao
         se (salary <= 4000.03) entao
            inssDescountPercent <- 12
         senao
            inssDescountPercent <- 14
         fimse
      fimse
   fimse
   transportDescount <- salary * (6 / 100)
   foodDescount <- salary * (6 / 100)
   inssDescount <-  salary * (inssDescountPercent / 100)
   liquidSalary <- salary
   se transportDescount > transportSalary entao
      transportDescount <- transportSalary
   fimse
   se (foodDescount > (foodSalary * (20/100))) entao
      foodDescount <- foodSalary
   fimse
   liquidSalary <- liquidSalary - transportDescount - inssDescount
fimfuncao

funcao getData() : caractere
inicio
   limpatela
   escreval("------ Dados do Funcionário ------")
   escreval("Nome: ", name)
   escreval("Quantidade de horas trabalhadas no mês: ", quantHours)
   escreval("Ssálario por hora: R$", salaryPerHour:2:2)
   escreval("Valor do vale transporte: R$", transportSalary:2:2)
   escreval("Valor do vale de alimentação: R$", foodSalary:2:2)
   escreval("Salário bruto: R$", salary:2:2)
   escreval("Salário liquido: R$", liquidSalary:2:2)
   escreval("Desconto do INSS: %", inssDescountPercent)
   escreval("Valor do desconto do INSS: R$", inssDescount:2:2)
   escreval("Desconto do vale transporte: R$", transportDescount:2:2)
   escreval("Desconto do vale alimentação: R$", foodDescount:2:2)
fimfuncao

Inicio
   escreval("### FOLHA DE PAGAMENTO ###")
   escreva("Digite quantos funcionários você deseja consultar: ")
   leia(quantEmployee)
   para i de 1 ate quantEmployee faca
      escreval(cadastro)
      escreval(getData)
   fimpara
Fimalgoritmo