from helper.writeAJson import writeAJson

def totalVendas(db):
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$group": {"_id": None, "Total": {"$sum": "$total"}}}
    ])
    writeAJson(result, "Total de Vendas")


def maisVendido(db):
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])
    writeAJson(result, "Produto mais vendido")
    
def maiorGasto(db):
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])
    writeAJson(result, "Cliente que mais gastou")
    
def maisDeUmaVenda(db):
    result = db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 1}}},
        {"$project": {"_id": 0, "descricao": "$produtos.descricao", "quantidade": "$produtos.quantidade"}},
        {"$sort": {"total": -1}}
    ])
    writeAJson(result, "Produtos vendidos")