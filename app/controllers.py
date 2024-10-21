from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['test']
collections = db['people']

# buscar
query = collections.find()

# adicionar
#collections.insert_one({
#    "name":"Ludwig",
#    "age": "55"
#})

# exibir
for document in query:
    print(document)

# atualizar
#collections.update_one(
#    {"name":"Ludwig"},
#    {'$set': {'age': 11}}
#)

# deletar
# collections.delete_one({'name': 'Ludwig'})


def add_people(jsonPeople):
    collections.insert_one(jsonPeople)



mima = {
    "name":"Mima Valentina",
    "age": "6"
}

feu = {
    "name":"Morfeu",
    "age": 7
}

#add_people(mima)
#add_people(feu)
print()


"""
Filtros:

Operador	Descrição	Exemplo
$eq	Igual a	{'age': {'$eq': 30}}
$ne	Diferente de	{'age': {'$ne': 30}}
$gt	Maior que	{'age': {'$gt': 30}}
$gte	Maior ou igual a	{'age': {'$gte': 30}}
$lt	Menor que	{'age': {'$lt': 30}}
$lte	Menor ou igual a	{'age': {'$lte': 30}}
$in	Dentro de um conjunto	{'age': {'$in': [25, 30, 35]}}
$nin	Não dentro de um conjunto	{'age': {'$nin': [25, 30, 35]}}
$exists	Verifica se um campo existe	{'age': {'$exists': True}}
$regex	Expressão regular	{'name': {'$regex': '^J'}}
Operações de atualização:

Operador	Descrição	Exemplo
$set	Define um novo valor para um campo	{'$set': {'age': 31}}
$inc	Incrementa um campo numérico	{'$inc': {'age': 1}}
$push	Adiciona um elemento a um array	{'$push': {'interests': 'sports'}}
$pull	Remove um elemento de um array	{'$pull': {'interests': 'sports'}}
$addToSet	Adiciona um elemento a um array se ele não existir	{'$addToSet': {'interests': 'sports'}}
Operações de agregação:

Operador	Descrição	Exemplo
$match	Filtra documentos	{'$match': {'age': {'$gt': 30}}}
$group	Agrupa documentos	{'$group': {'_id': '$age', 'count': {'$sum': 1}}}
$project	Seleciona campos	{'$project': {'name': 1, 'age': 1, '_id': 0}}
$sort	Ordena documentos	{'$sort': {'age': 1}}
$limit	Limita o número de documentos	{'$limit': 10}
$skip	Pula um número de documentos	{'$skip': 10}
"""