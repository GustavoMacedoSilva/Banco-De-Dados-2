from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()
#-------------
def getPokemonByName(name: str):
    return db.collection.find({"name": name})

pikachu = getPokemonByName("Vaporeon")
writeAJson(pikachu, "Vaporeon")
#-----------
def getPokemonsByType(types: list):
    return db.collection.find({"type": {"$in": types}})

types = ["Water", "Fire"]
pokemons = getPokemonsByType(types)

writeAJson(pokemons, "pokemons_fogo_agua")
#-------------
fraquezas = ["Water", "Fire"]
pokemons = db.collection.find({"weaknesses": {"$all": fraquezas}})
writeAJson(pokemons, "pokemons_fracos_agua_fogo")

#----------
tipos = ["Water", "Fire"]
pokemons = db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })
writeAJson(pokemons, "pokemons_agua_fogo_evolucao")

#-------
pokemons = db.collection.find({"multipliers": 2.12})
writeAJson(pokemons, "pokemons_multipliers_2.12")