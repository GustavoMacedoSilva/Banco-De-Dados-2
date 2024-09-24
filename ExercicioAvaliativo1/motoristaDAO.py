from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, corridas:dict, nota:int):
        # Montando o documento a ser inserido
        motorista_document = {
            "nota": nota,
            "corridas": [
                {
                    "passageiro": 
                    {
                    "nome": corrida.passageiro.nome,
                    "Documento do Passageiro": corrida.passageiro.documento,
                    },
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "nota": corrida.nota  # Inclua outros atributos que você queira
                }
                for corrida in corridas
            ]
        }
        # Inserindo o documento no banco de dados
        try:
            res = self.db.collection.insert_one(motorista_document)
            print(f"Motorista criado com sucesso: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista achado: {res}")
            return res
        except Exception as e:
            print(f"Um erro ocorreu ao procurar motorista: {e}")
            return None

    def update_motorista(self, id:str, corridas:dict, nota:int):
        try:
            corridas_dicts = [corrida.to_dict() for corrida in corridas]
        
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"corridas": corridas_dicts, "nota": nota}}
            )
        
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificados")
            return res.modified_count
        except Exception as e:
            print(f"Um erro ocorreu ao atualizar um motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Um erro ocorreu ao deletar o motorista: {e}")
            return None