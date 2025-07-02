class Livro:
    id = 0
    
    def __init__(self, titulo, autor, quant_paginas):
        self.id = Livro.id
        self.titulo = titulo
        self.autor = autor
        self.quant_paginas = quant_paginas 
        self.pagina_atual = 0
        self.status = ""
        
    def get_id(self):
        return self.id

    def atualizar_status(self, percentual):
        if percentual == 0:
            self.status = "Leitura não iniciada"
        elif percentual < 100:
            self.status = "Leitura em curso"
        else:
            self.status = "Leitura encerrada"
        return self.status
    
    def get_status(self):
        return self.status

    def get_quant_paginas_restantes(self):
        quant_paginas_restantes = self.quant_paginas - self.pagina_atual
        return quant_paginas_restantes
    
    def marcar_pagina(self, pagina):
        self.pagina_atual = pagina
        return self.pagina_atual
    
    def get_percentual_leitura(self):
        self.percentual_leitura = (self.pagina_atual * 100) / self.quant_paginas
        return self.percentual_leitura
    
    def get_pagina_atual(self):
        return self.pagina_atual
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_quant_paginas(self):
        return self.quant_paginas 
    
    def __str__(self):
        return f"Livro [ID = {self.get_id()}, titulo = {self.get_titulo()}, autor = {self.get_autor()}, quant_paginas = {self.get_quant_paginas()}]"