from programa import Programa

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self.duracao = duracao
        super().__init__(nome, ano)
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'
