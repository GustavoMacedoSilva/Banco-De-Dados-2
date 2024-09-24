from corrida import Corrida
from passageiro import Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_DAO):
        super().__init__()
        self.motorista_DAO = motorista_DAO
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        try:
            corridas=[]
            
            num_corridas = int(input("Quantas corridas voce deseja adicionar: "))

            for i in range(num_corridas):
                nome_passageiro = input("Digite o nome do passageiro: ")
                documento_passageiro = input("Qual o documento do passageiro: ")
                passageiro_aux = Passageiro(nome_passageiro, documento_passageiro)
                print(f"\nCorrida {i + 1}:")
                nota = int(input("Nota da corrida: "))
                distancia = float(input("Distancia da corrida: "))
                valor = float(input("Valor da corrida: "))
                
                corrida_aux = Corrida(nota, distancia, valor, passageiro_aux)
                corridas.append(corrida_aux)
            
            motorista_id = self.motorista_DAO.create_motorista(corridas, nota)
        
            print(f"Motorista criado com ID: {motorista_id}")

        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")


    def read_motorista(self):
        id = input("Digite o id do motorista: ")
        try:
            motorista = self.motorista_DAO.read_motorista_by_id(id)
        
            if motorista:
                print(f"Nota: {motorista['nota']}")

                if 'corridas' in motorista and isinstance(motorista['corridas'], list):
                    print("Corridas:")
                
                    for i, corrida in enumerate(motorista['corridas'], start=1):
                        print(f"Corrida {i}:")
                        for key, value in corrida.items():
                            print(f"  {key}: {value}")
                else:
                    print("Nenhuma corrida encontrada.")
            else:
                print("Motorista não encontrado.")
    
        except Exception as e:
            print(f"Ocorreu um erro ao ler o motorista: {e}")


def update_motorista(self):
    try:
        id = input("Escreva o ID do motorista: ")
        corridas_existentes = self.motorista_DAO.get_corridas_by_motorista_id(id)

        corridas_atualizadas = corridas_existentes.copy()

        adicionar_corridas = input("Deseja adicionar novas corridas? (s/n): ").strip().lower()
        
        deletar_corrida = input("Deseja deletar uma corrida existente? (s/n): ").strip().lower()
        if deletar_corrida == 's':
            corrida_index = int(input("Digite o número da corrida a ser deletada: ")) - 1
            if 0 <= corrida_index < len(corridas_existentes):
                del corridas_existentes[corrida_index]
                print("Corrida deletada com sucesso.")
            else:
                print("Índice de corrida inválido.")

        
        if adicionar_corridas == 's':
            num_corridas = int(input("Quantas corridas você deseja adicionar: "))
            for i in range(num_corridas):
                nome_passageiro = input("Digite o nome do passageiro: ")
                documento_passageiro = input("Qual o documento do passageiro: ")
                passageiro_aux = Passageiro(nome_passageiro, documento_passageiro)
                print(f"\nCorrida {i + 1}:")
                nota = int(input("Nota da corrida: "))
                distancia = float(input("Distância da corrida: "))
                valor = float(input("Valor da corrida: "))
                
                corrida_aux = Corrida(nota, distancia, valor, passageiro_aux)
                corridas_atualizadas.append(corrida_aux)

        
        nova_nota = int(input("Escreva a nova nota: "))
        self.motorista_DAO.update_motorista(id, corridas_atualizadas, nova_nota)

        print(f"Motorista com ID {id} atualizado com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o motorista: {e}")

    def delete_motorista(self):
        id = input("Escreva o id do motorista: ")
        self.motorista_DAO.delete_motorista(id)
        
    def run(self):
        print("Welcome to the person CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        
