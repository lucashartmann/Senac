Algoritmo "Escola"

Var

   quantAulas, quantPresenca, quantFaltas, quantNotas : inteiro
   idade, numero, user, cadastro, matricula, quant : inteiro
   quantAlunos, quantProfessores, presenca, index : inteiro
   numCadastrosProfessores, matriculasCadastradas: vetor[1..10] de inteiro
   nomesAlunos, nomesProfessores, materias : vetor[1..10] de caractere
   nome, cpf, rg, turma, teclaApertada, materia : caractere
   notasGeral, notasMateria : vetor[1..10] de real
   media, soma, nota : real
   verifica: logico

procedimento menuUsuario()
inicio
   numero <- 0
   enquanto (numero < 1) ou (numero > 8) faca
      escreval("####### MENU #######")
      escreval()
      escreval("1 -- Ver frequência")
      escreval("2 -- Ver média")
      escreval("3 -- Ver soma")
      escreval("4 -- Ver todas as notas")
      escreval("5 -- Ver notas de certa matéria")
      escreval("6 -- Ver todas as materias")
      escreval("7 -- Pedir atestado de matrícula")
      escreval("8 -- Sair do menu")
      escreval()
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escreval()
      escolha(numero)
      caso 1
         escreval("Você escolheu ver frequência")
         escreval("Aulas dadas: ", quantAulas)
         escreval("Presença: ", quantPresenca)
         escreval("Faltas: ", quantFaltas)
         numero <- 0
      caso 2
         escreval("Você escolheu ver media")
         se (soma <= 0) entao
            soma <- somaGeral
         fimse
         escreval("Média: ", media(soma, quantNotas))
         numero <- 0
      caso 3
         escreval("Você escolheu ver soma")
         soma <- somaGeral
         escreval("Soma: ", soma))
         numero <- 0
      caso 4
         escreval("Você escolheu ver todas as notas")
         escreva("Notas: ")
         para index de 1 ate quant faca
            escreva(notasGeral[index], "")
         fimpara
         escreval()
         numero <- 0
      caso 5
         escreval("Você escolheu ver notas de certa materia")
         escreva("Notas: ")
         para index de 1 ate quant faca
            escreva(notasMateria[index], "")
         fimpara
         escreval()
         numero <- 0
      caso 6
         escreval("Você escolheu ver todas as materias")
         dadosMaterias
         numero <- 0
      caso 7
         escreval("Você escolheu pedir atestado de matricula")
         atestado
         numero <- 0
      caso 8
         escreval("Você escolheu sair")
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
fimprocedimento

procedimento menuProfessor()
inicio
   numero <- 0
   enquanto((numero < 1) ou (numero > 3)) faca
      escreval("####### MENU #######")
      escreval()
      escreval("1 -- Cadastrar notas")
      escreval("2 -- Cadastrar frequencia")
      escreval("3 -- Sair do menu")
      escreval()
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escreval()
      escolha(numero)
      caso 1
         escreval("Você escolheu cadastrar notas")
         cadastarNotas
         numero <- 0
      caso 2
         escreval("Você escolheu cadastrar frequencia")
         cadastrarFrequencia
         numero <- 0
      caso 3
         escreval("Você escolheu sair")
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
fimprocedimento

procedimento menuAdmin()
inicio
   numero <- 0
   enquanto (numero < 1) ou (numero > 5) faca
      escreval("####### MENU #######")
      escreval()
      escreval("1 -- Cadastrar aluno")
      escreval("2 -- Cadastrar professor")
      escreval("3 -- Editar dados")
      escreval("4 -- Ver dados")
      escreval("5 -- Sair do menu")
      escreval()
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escreval()
      escolha(numero)
      caso 1
         escreval("Você escolheu cadastrar aluno")
         cadastarAluno
         numero <- 0
      caso 2
         escreval("Você escolheu cadastrar professor")
         cadastarProfessor
         numero <- 0
      caso 3
         escreval("Você escolheu editar")
         editar
         numero <- 0
      caso 4
         escreval("Você escolheu ver dados")
         dados
         numero <- 0
      caso 5
         escreval("Você escolheu sair")
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
fimprocedimento

procedimento cadastarAluno()
inicio
   quant <- 0
   escreva("Quantos alunos deseja cadastrar: ")
   leia(quant)
   quantAlunos <- quantAlunos + quant
   para index de 1 ate quant faca
      matricula <- matricula + 1
      escreva("Informe o nome do aluno: ")
      leia(nome)
      nomesAlunos[index] <- nome
      aleatorio on
      aleatorio 1, matricula
      leia (matricula)
      aleatorio off
      matriculasCadastradas[index] <- matricula
   fimpara
fimprocedimento

procedimento cadastarProfessor()
inicio
   quant <- 0
   escreva("Quantos professores deseja cadastrar: ")
   leia(quant)
   quantProfessores <- quantProfessores + quant
   para index de 1 ate quant faca
      cadastro <- cadastro + 1
      escreva("Informe o nome do professor: ")
      leia(nome)
      escreva("Informe a materia do professor: ")
      leia(materia)
      materias[index] <- materia
      nomesProfessores[index] <- nome
      aleatorio on
      aleatorio 1, cadastro
      leia (cadastro)
      aleatorio off
      numCadastrosProfessores[index] <- cadastro
   fimpara
fimprocedimento

procedimento cadastarNotas()
inicio
   quant <- 0
   escreva("Quantos notas deseja cadastrar: ")
   leia(quant)
   quantNotas <- quantNotas + quant
   para index de 1 ate quant faca
      escreva("Informe a nota : ")
      leia(nome)
      notasMateria[index] <- nota
      notasGeral[index] <- nota
   fimpara
fimprocedimento

procedimento dados()
inicio
   escreval("Notas: ")
   para index de 1 ate quantNotas faca
      escreval(notasMateria[index], " ")
      escreva(notasGeral[index], " ")
   fimpara
   escreval()
   escreval("Alunos: ")
   para index de 1 ate quantAlunos faca
      escreval("Nome: ", nomesAlunos[index])
      escreval("Matricula: ", matriculasCadastradas[index])
   fimpara
   escreval()
   escreval("Professores: ")
   para index de 1 ate quantProfessores faca
      escreval("Nome: ", nomesProfessores[index])
      escreval("Cadastro: ", numCadastrosProfessores[index])
      escreval("Matéria: ", materias[index])
   fimpara
fimprocedimento

procedimento dadosMaterias()
inicio
   para index de 1 ate quantProfessores faca
      escreval("Matéria: ", materias[index])
      escreval("Professor: ", nomesProfessores[index])
   fimpara
fimprocedimento

procedimento editar()
inicio
   escreval("1 -- Aluno")
   escreval("2 -- Professor")
   escreval("Digite o número corresponde ao que voce deseja editar: ")
   leia(number)
   escreval("Escreva o nome da pessoa desejada: ")
   leia(nome)
   verifica <- falso
   se(number == 1) entao
      para index de 1 ate quantAlunos faca
         se(nomesAlunos[index] = nome)
            escreval("Digite o novo nome desejado: ")
            leia(nome)
            nomesAlunos[index] <- nome
            verifica <- verdadeiro
         fimse
      fimpara
   senao
      para index de 1 ate quantProfessores faca
         se(nomesProfessores[index] = nome)
            escreval("Digite o novo nome desejado: ")
            leia(nome)
            nomesProfessores[index] <- nome
            verifica <- verdadeiro
         fimse
      fimpara
   fimse
   se (verifica = falso) entao
      escreval("Pessoa não está cadastrada")
   fimse
fimprocedimento

procedimento atestado()
inicio
   escreval("Ensino Médio 2024")
   escreval("Nome do aluno: ")
   escreval("Matricula do aluno: ")
   escreval("CPF: ")
   escreval("RG: ")
   escreval("Materias: ")
fimprocedimento

funcao cadastrarFrequencia() : inteiro
inicio
   escreva("Quantas aulas foram dadas? ")
   leia(quantAulas)
   escreva("Quantas aulas o aluno esteve presente? ")
   leia(quantPresenca)
   quantFaltas <- quantAulas - quantPresenca
   retorne quantPresenca
fimfuncao

funcao media(soma : real; quant : inteiro) : real
inicio
   media <- soma / quant
   retorne media
fimfuncao

funcao somaGeral() : real
inicio
   para index de 1 ate quantNotas faca
      soma <- soma + notasGeral[index]
   fimpara
   retorne soma
fimfuncao

Inicio
   escreval("Escola Santo Joaquim")
   escreval()
   escreval("Aperte uma tecla")
   leia(teclaApertada)
   limpatela
   numero <- 0
   enquanto (numero < 1) ou (numero > 4) faca
      limpatela
      escreval("####### LOGIN #######")
      escreval("1 -- Aluno")
      escreval("2 -- Professor")
      escreval("3 -- Admin")
      escreval("4 -- Sair")
      escreva("Digite o número correspondente a opção desejada: ")
      leia(numero)
      escolha(numero)
      caso 1
         escreval("Você escolheu aluno")
         escreva("Informe sua matrícula: ")
         leia(matricula)
         para index de 1 ate quantAlunos faca
            se(matriculaCadastradas[index] = matricula)
               user <- 1
            fimse
         fimpara
         se(user = 1) entao
            menuUsuario
         senao
            escreval("Você não está cadastrado. Contate um admin")
         fimse
      caso 2
         escreval("Você escolheu professor")
         escreva("Informe seu número de cadastro: ")
         leia(cadastro)
         para index de 1 ate quantProfessores faca
            se(numCadastrosProfessores[index] = cadastro)
               user <- 2
            fimse
         fimpara
         se(user = 2) entao
            menuProfessor
         senao
            escreval("Você não está cadastrado. Contate um admin")
         fimse
      caso 3
         escreval("Você escolheu admin")
         user <- 3
         menuAdmin
      caso 4
      outrocaso
         escreval("Número inválido. Tente novamente")
      fimescolha
   fimenquanto
   limpatela

Fimalgoritmo