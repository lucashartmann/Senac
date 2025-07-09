class Filme:
    def __init__(self):
        self.alugado = False
        self.em_acervo = True
        self.valor = 0.0
        self.classificacao_etaria = ""        
        self.genero = ""
        self.categoria = Categoria()

class Categoria:
    def __init__(self):
        self.nome = ""
        self.multa_por_dano = 0.0

class Cliente:
    def __init__(self):
        self.nome = ""
        self.filmes_escolhidos = []  

class Aluguel:
    def __init__(self, cliente):
        self.cliente = cliente
        self.filmes = []
        self.data_retirada = ""
        self.data_devolucao = ""
        self.valor = 0.0
        self.juros_por_atraso = 0.0

class Funcionario():
    pass

class Locadora():
    pass

def alugar_filme():
    '''o cliente 
        - identifica-se para a locadora
       a locadora
        - valida o cliente        - 
       o cliente
        - escolhe os filmes na prateleira
        - dirige-se ao funcionário com os filmes
        - identifica-se ao funcionário
       o funcionário        
        - registra os alugueis dos filmes no sistema/locadora
       a locadora
        - recebe os registros de aluguel fornecidos pelo funcionário
        - calcula os prazos de devolução
        - calcula o valor total dos alugueis
        - retorna ao funcionário os registros de aluguel preenchidos
      o funcionario
        - recebe registros preenchidos
        - dá ao cliente um comprovante do aluguel com o valor total lido nos registros
    '''

    um_cliente = Cliente()
    a_locadora = Locadora()
    um_funcionario = Funcionario()

    a_locadora.validar(um_cliente)
    filmes_disponiveis = a_locadora.mostrar_filmes_da_prateleira()
    um_cliente.escolher(filmes_disponiveis)
    um_funcionario.receber_filmes(um_cliente.filmes_escolhidos)
    a_locadora.preencher_registros_de_aluguel(um_funcionario.filmes_para_alugar)
    um_cliente.receber_comprovante(um_funcionario.




