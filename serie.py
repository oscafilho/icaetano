from programa import Programa

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self.temporadas = temporadas
        super().__init__(nome, ano)
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'