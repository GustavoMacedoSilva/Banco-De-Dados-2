class Corrida:
    def __init__(self, nota:int, distancia:float, valor:float, passageiro:object):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro
        
        
        
    def to_dict(self):
        return {
            "distancia": self.distancia,
            "nota": self.nota,
            "valor": self.valor,
            "passageiro": {
                "nome": self.passageiro.nome,
                "documento": self.passageiro.documento
            }
        }