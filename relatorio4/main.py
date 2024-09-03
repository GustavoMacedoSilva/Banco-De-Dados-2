from database import Database
from helper.writeAJson import writeAJson
from ProductAnalyzer import *

db = Database(database="mercado", collection="produtos")
#db.resetDatabase()

#totalVendas(db)
#maisVendido(db)
#maiorGasto(db)
maisDeUmaVenda(db)