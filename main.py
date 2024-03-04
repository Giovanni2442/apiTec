from flask import Flask,jsonify,render_template,request
from ussers import Ussers
import database as dbase    #importa la conceción a la bd
from bson.json_util import dumps , ObjectId  # Agrega la importación de dumps desde bson.json_util

#Conección a la base de datos
db = dbase.dbConnection()

app = Flask(__name__, template_folder='templates')

#---Rutas de la Aplicación---
@app.route("/index")
def index():
    return render_template("Index.html")

#---Peticiones REST---
#GET ALL
@app.route("/getUssers")
def getAll():
    try:
        
        collection = db['ussers']
        getAll = collection.find()
        result = dumps(getAll) #converter the cursor seriarizable to json
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
    
#GET id
@app.route("/getUsser/<id>")
def getOne(id):
    try:
        collection = db['ussers']
        usser_id = ObjectId(id)
        getOne = collection.find_one({'_id' : usser_id})
        result = dumps(getOne)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
    
#POST
@app.route("/addUsser", methods = ['POST'])
def addUsser():
    try:
        collection = db['ussers']
        name = request.json["name"] 
        lstnF = request.json["lstnF"]
        lstnM = request.json["lstnM"]
        age = request.json["age"]
        email = request.json["email"]
        city = request.json["city"]
        uss = Ussers(name=name,
                     lstnF=lstnF,
                     lstnM=lstnM,
                     age=age,
                     email=email,
                     city=city)
        collection.insert_one(uss.collectionUssers())
        #result = dumps(insertUssr)
        return 'Save Ok'
    except Exception as e:
        return jsonify({'error': str(e) })
    
#PUT
@app.route("/addUsser", methods = ['POST'])
def UpdateUsser():
    try:
        collection = db['ussers']
        name = request.json["name"] 
        lstnF = request.json["lstnF"]
        lstnM = request.json["lstnM"]
        age = request.json["age"]
        email = request.json["email"]
        city = request.json["city"]
        uss = Ussers(name=name,
                     lstnF=lstnF,
                     lstnM=lstnM,
                     age=age,
                     email=email,
                     city=city)
        collection.update_one(uss.collectionUssers())
        #result = dumps(insertUssr)
        return 'Save Ok'
    except Exception as e:
        return jsonify({'error': str(e) })

#DELETE
@app.route('/deleteUsser/<id>', methods = ['DELETE'])
def deleteUsser(id):
    try:
        collection = db['ussers']
        usser_id = ObjectId(id)
        collection.delete_one({'_id': usser_id})
        return 'delete Ok'
    except Exception as e:
        return jsonify({'error': str(e)})

#Levanta el servidor con un puerto en especifico
if __name__ == '__main__':
    app.run(None,2000,debug=True)