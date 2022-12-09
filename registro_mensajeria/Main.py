from flask import Flask, render_template, request
from pymongo import MongoClient, database

url = render_template

cliente = MongoClient('localhost', port=27017)

database = cliente["PeliculasFavoritas"]

movies = database.movies

app = Flask(__name__)

@app.route('/')
def Home():
    return url('/index.html')

@app.route('/usuario', methods=['POST'])
def usuario():
    NombreUsuario = request.form['Nombre']
    EdadUsuario = request.form['Edad']
    PeliculaUsuario = request.form['Pelicula']

    movie_ = {
        "usuario": NombreUsuario,
        "edad": EdadUsuario,
        "Pelicula": PeliculaUsuario
    }
    id = movies.insert_one(movie_).inserted_id

    print(id)

    return url('/recibido.html')

if __name__ == "__main__":

    #EL DEBUG ACTUALIZA EL MAIN SIN REINICIAR EL SERVER
    app.run(host='localhost', port=3102, debug = True) 
