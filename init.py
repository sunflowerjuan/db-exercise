from flask import Flask, jsonify
from pymongo import MongoClient

# Conexión como root a MongoDB
client = MongoClient("mongodb://juan:102210@localhost:27017/?authSource=admin")
db = client["personas"]

# Crear aplicación Flask
app = Flask(__name__)

# Endpoint para inicializar la base de datos
@app.route("/init")
def init_db():
    db.personas.insert_one({"nombre": "Julian", "estado": "deprimido"})
    db.personas.insert_one({"nombre": "Tonny", "estado": "Feliz"})
    db.personas.insert_one({"nombre": "Majo", "estado": "Majo"})
    return jsonify({"mensaje": "Base de datos inicializada con exito"})

# Endpoint para listar todos los documentos
@app.route("/personas")
def listar_personas():
    personas = list(db.personas.find({}, {"_id": 0}))
    return jsonify(personas)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
