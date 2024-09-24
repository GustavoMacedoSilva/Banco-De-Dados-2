from database import Database
from writeAJson import writeAJson
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI
from corrida import Corrida
from passageiro import Passageiro

db = Database(database="BD2-EA", collection="motoristas")
motoristaDAO = MotoristaDAO(database=db)

passageiro1 = Passageiro("sds", "F00432-C23")
#passageiro2 = Passageiro("Marcos", "FEOODO3993-22")
#passageiro3 = Passageiro("Jose", "IDBHN33JJ-00")

corrida1 = Corrida(4, 35.78, 53.45, passageiro1)
#corrida2 = Corrida(4, 300, 100.00, passageiro2)
#corrida3 = Corrida(3, 400, 999.00, passageiro3)

corridas1 = [corrida1]

motoristaDAO.create_motorista(corridas1, 2)

#motoristaDAO.delete_motorista("66f1f0f54da71bdfcc2c0f4b")

#motoristaDAO.read_motorista_by_id("66f1f32f3f345e9706db84c0")

#motoristaDAO.update_motorista("66f1f32f3f345e9706db84c0", corridas1, 3)
#motoristaDAO.read_motorista_by_id("66f1f32f3f345e9706db84c0")


#motoristaDAOCLI = MotoristaCLI(motoristaDAO)
#motoristaDAOCLI.run()