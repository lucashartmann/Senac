from models import Locomotiva, Vagao, Trem


class Trem:
    id = 0

    def __init__(self):
        self.id = Trem.id
        # self.quant_vagoes = 0
        # self.quant_locomotivas = 0
        # self.quant_max_vagoes_suportados = 0
        # self.quant_max_locomotivas_suportados = 0
        self.peso_suportado = 200000.00
        self.peso_atual = 0
        self.trem = []

    def gerar_id(self):
        Trem.id += 1
        return Trem.id

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            return 0

    def get_locomotivas(self):
        locomotivas = []
        for veiculo in self.trem:
            if type(veiculo) == Locomotiva.Locomotiva:
                locomotivas.append(veiculo)
        return locomotivas

    def get_vagoes(self):
        vagoes = []
        for veiculo in self.trem:
            if type(veiculo) == Vagao.Vagao:
                vagoes.append(veiculo)
        return vagoes
    
    def get_peso_suportado(self):
        try:
            return self.peso_suportado
        except AttributeError:
            return 0

    def get_peso_atual(self):
        try:
            return self.peso_atual
        except AttributeError:
            return 0

    def engatar(self, veiculo):
        peso_total = self.peso_atual + veiculo.get_peso()
        if (type(veiculo) == Locomotiva.Locomotiva or type(veiculo) == Vagao.Vagao) and veiculo not in self.trem and peso_total <= self.peso_suportado:
            self.peso_atual += veiculo.get_peso()
            self.trem.append(veiculo)
            return True
        return False

    def desengatar(self, veiculo):
        lista_veiculos = []
        try:
            index_veiculo = self.trem.index(veiculo)
            ultimo_index = len(self.trem) - 1
            if index_veiculo == ultimo_index:
                self.trem.remove(veiculo)
                self.peso_atual -= veiculo.get_peso()
            else:
                for veiculo_ferroviario in self.trem[index_veiculo:]:
                    self.trem.remove(veiculo_ferroviario)
                    self.peso_atual -= veiculo_ferroviario.get_peso()
                    lista_veiculos.append(veiculo_ferroviario)
            return (True, lista_veiculos)
        except ValueError:
            return (False, lista_veiculos)

    def get_trem(self):
        try:
            return self.trem
        except AttributeError:
            return []

    def esvaziar(self):
        self.trem.clear()
        
    def get_veiculo_por_id(self, id):
        for veiculo in self.trem:
            if veiculo.get_id() == id:
                return veiculo
        return None

    def possui_locomotiva(self):
        for veiculo in self.trem:
            if type(veiculo) == Locomotiva.Locomotiva:
                return True
        return False
    
    def get_quant_veiculos(self):
        cont = 0
        for veiculo in self.trem:
            cont += 1
        return cont

    def __str__(self):
        if self.get_quant_veiculos() > 0:
            string_veiculo = " <- ".join(str(veiculo) for veiculo in self.get_trem())
            return f"Trem [id = {self.get_id()}, peso: {self.get_peso_atual()}]: [{string_veiculo}] "
        return f"Trem [id = {self.get_id()}] = []"