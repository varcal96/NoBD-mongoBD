from pymongo import MongoClient

cliente = MongoClient('localhost', port=27017)

database = cliente['PeliculasFavoritas']

coleccion = database['movies']

results = coleccion.find()

for i in results:
    print('A-A: ', i['usuario'], '\tA-B: ', i['edad'], '\tA-C: ', i['Pelicula'])
    