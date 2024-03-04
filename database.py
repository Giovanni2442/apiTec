import pymongo 
myClient = "mongodb://localhost:27017"

def dbConnection():
    try:
        connect = pymongo.MongoClient(myClient)
        db = connect["test"]
        return db
    except ConnectionError:
        return 'Error al conectar con la db'
        
print(dbConnection())

