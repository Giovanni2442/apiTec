import json
import os
from flask import Flask, app,jsonify ,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

#app.config['MYSQL_HOST'] = "host.docker.internal"  #host.docker.internal
#app.config['MYSQL_USER'] = 'root'                   
#app.config['MYSQL_PASSWORD'] = '2442'
#app.config['MYSQL_PORT'] = 13308
#app.config['MYSQL_DB'] = 'db_tec'

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3306))
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

db = MySQL(app) 

@app.route('/consulta/<int:id>', methods=['GET'])
def obtener_consulta(id):
    cur = db.connection.cursor()
    try:
        cur.execute("""
            SELECT 
                JSON_OBJECT('id',c.id,'name',c.name,
                    'reticula',(
                        SELECT
                            json_arrayagg(
                                json_object(
                                    'id',r.id,
                                    'clave',r.clave,
                                    'nombre',r.nombre,
                                    'creditos',r.creditos,
                                    'semestre',r.semestre))
                        FROM db_tec.reticula r
                        WHERE r.carrera_id = c.id 
                    ),
                    'especialidades',(
                        SELECT 
                            json_arrayagg(
                                json_object(
                                    'id',e.id,
                                    'nombre',e.name,
                                    'materias',(
                                        SELECT 
                                            json_arrayagg(
                                                json_object(
                                                    'Id',m.id,
                                                    'nombre',m.nombre,
                                                    'semestre',m.Semestre,
                                                    'creditos',m.creditos))
                                        FROM 
                                            db_tec.materias m , db_tec.especialidades e
                                        WHERE m.especialidad_id = e.id)
                                    ))
                        FROM 
                            db_tec.especialidades e 
                        WHERE e.carrera_id = c.id
                    )
                )
                AS dato
                FROM carrera c
                where c.id =1;SELECT 
                JSON_OBJECT('id',c.id,'name',c.name,
                    'reticula',(
                        SELECT
                            json_arrayagg(
                                json_object(
                                    'id',r.id,
                                    'clave',r.clave,
                                    'nombre',r.nombre,
                                    'creditos',r.creditos,
                                    'semestre',r.semestre))
                        FROM db_tec.reticula r
                        WHERE r.carrera_id = c.id 
                    ),
                    'especialidades',(
                        SELECT 
                    
                            json_arrayagg(
                                json_object(
                                    'id',e.id,
                                    'nombre',e.name,
                                    'materias',(
                                        SELECT 
                                            json_arrayagg(
                                                json_object(
                                                    'Id',m.id,
                                                    'nombre',m.nombre,
                                                    'semestre',m.Semestre,
                                                    'creditos',m.creditos))
                                        FROM 
                                            db_tec.materias m
                                        WHERE m.especialidad_id = e.id) -- Filtro por el id de la especialidad actual
                                    ))
                        FROM 
                            db_tec.especialidades e 
                        WHERE e.carrera_id = c.id
                    )
                )
                AS dato
                FROM carrera c
                WHERE c.id = 4;""")

        resultado = cur.fetchone()
        resultado_json = json.loads(resultado[0])
        return jsonify(resultado_json)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cur.close()

#---- GET'S ----
@app.route('/carrera',methods = ['GET'])
def getCarrera():
    cur = db.connection.cursor()
    cur.execute('SELECT * FROM especialidades;')
    data = cur.fetchall()
    result = []
    for i in data:
        content = {
            'id': i[0],
            'carrera_id': i[1],
            'name' : i[2] }
        
        result.append(content)
    return jsonify(result)

#---- POST´S ----
@app.route('/carrera', methods=['POST'])
def addCarrera():
    try:
        data = request.json
        carrera_id = data['id']
        carrera_nombre = data['ingenieria']

        cur = db.connection.cursor()
        cur.execute("INSERT INTO carrera (id, name) VALUES (%s, %s)", (carrera_id, carrera_nombre))
        db.connection.commit()
        return jsonify({"message": "Datos insertados correctamente."}), 200

    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    
@app.route('/reticula', methods=['POST'])
def addReticula():
    try:
        data = request.json

        mtriaId = data['id']    #id de la materia de la reticula
        carrera_id = data['carreraId']
        clave = data['clave']
        nombre = data['nombre']
        creditos = data['creditos']
        semestre = data['semestre']

        cur = db.connection.cursor()
        #INSERT INTO reticula (id,carrera_id,clave,nombre,creditos,semestre) VALUES (1,1,'ACF0901','Calculo Diferencial',5,1);
        cur.execute("INSERT INTO reticula (id,carrera_id,clave,nombre,creditos,semestre) VALUES (%s, %s, %s, %s, %s, %s)", (mtriaId,carrera_id,clave,nombre,creditos,semestre))
        db.connection.commit()
        return jsonify({"message": "Datos insertados correctamente."}), 200

    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/espc', methods=['POST'])
def addEspc():
    try:
        data = request.json

        espcId = data['id']
        carrera = data['carrera']
        name = data['name']

        cur = db.connection()
        #            INSERT INTO especialidades (id,carrera_id,name) VALUES (1,1,'Redes Emergentes');
        cur.execute("INSERT INTO especialidades (id,carrera_id,name) VALUES (%s,%s,%s)", (espcId,carrera,name))

    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500

@app.route('/espcMtrs', methods=['POST'])
def addEspcMtrs():
    try:
        data = request.json

        mtrEspId = ['id']
        espcId = data['idEspc']
        clave = data['clave']
        nombre = data['nombre']
        semestre = data['semestre']
        creditos = data['creditos']

        cur = db.connection.cursor()
        #            INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (1,2,'ACF0901','robotica_II',5,5);
        cur.execute("INSERT INTO materias (id,especialidad_id,clave,name,semestre,creditos) VALUES (%s, %s, %s, %s, %s)", (mtrEspId,espcId,clave,nombre,semestre,creditos))
        db.connection.commit()
        return jsonify({"message": "Datos insertados correctamente."}), 200

    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    

# ---- PUT´S ----

#---PUT---
@app.route('/carrera/<int:Id>', methods=['PUT'])
def UpdateCarrera(Id):
    try:
        data = request.json
        carrera_nombre = data['ingenieria']

        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("UPDATE carrera SET name = %s WHERE carrera.id = %s",(carrera_nombre,Id))
        db.connection.commit()
        return jsonify({"message": "Update Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    
#---PUT---
@app.route('/reticula/<int:Id>', methods=['PUT'])
def UpdateReticula(Id):
    try:
        data = request.json
        clave = data['clave']
        nombre = data['nombre']
        creditos = data['creditos']
        semestre = data['semestre']

        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("UPDATE reticula SET clave = %s, nombre = %s, creditos = %s, semestre = %s WHERE reticula.id = %s",(clave,nombre,creditos,semestre,Id))
        db.connection.commit()
        return jsonify({"message": "Update Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500

#---PUT---   
@app.route('/espc/<int:Id>', methods=['PUT'])
def UpdateEspc(Id):
    try:
        data = request.json
        
        name = data['name']

        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("UPDATE especialidades SET name = %s WHERE especialidades.id = %s",(name,Id))
        db.connection.commit()
        return jsonify({"message": "Update Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    
#---PUT---   
@app.route('/espcMtrs/<int:Id>', methods=['PUT'])
def UpdateEspcMtrs(Id):
    try:
        data = request.json
    
        clave = data['clave']
        nombre = data['nombre']
        semestre = data['semestre']
        creditos = data['creditos']

        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("UPDATE materias SET clave = %s, nombre = %s, semestre = %s, creditos = %s WHERE materias.id = %s",(clave,nombre,semestre,creditos,Id))
        db.connection.commit()
        return jsonify({"message": "Update Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500


# ---- DELETE´S ---- 

#--DELETE--
@app.route('/carrera/<int:Id>', methods=['PUT'])
def DltCarrera(Id):
    try:
        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("DELETE FROM carrera WHERE carrera.id = %s",(Id))
        db.connection.commit()
        return jsonify({"message": "Delete Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    
#--DELETE--
@app.route('/reticula/<int:Id>', methods=['PUT'])
def DltRetic(Id):
    try:
        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("DELETE FROM reticula WHERE reticula.id = %s",(Id))
        db.connection.commit()
        return jsonify({"message": "Delete Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    
#--DELETE--
@app.route('/espc/<int:Id>', methods=['PUT'])
def DltEspc(Id):
    try:
        data = request.json
        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("DELETE FROM especialidades WHERE especialidades.id = %s",(Id))
        db.connection.commit()
        return jsonify({"message": "Delete Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500
    
#--DELETE--
@app.route('/espcMtrs/<int:Id>', methods=['PUT'])
def DltEspcMtrs(Id):
    try:
        data = request.json
        cur = db.connection.cursor()
        # UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;
        cur.execute("DELETE FROM materias WHERE materias.id = %s",(Id))
        db.connection.commit()
        return jsonify({"message": "Delete Ok!"}), 200
    
    except Exception as e:
        # Si hay un error, se revierte la transacción
        return jsonify({"error": str(e)}), 500


# ---- PRUEBAS ----
@app.route('/insert2', methods=['POST'])
def insert_data():
    try:
        data = request.json
        
        # Extraer datos del JSON
        carrera_id = data['id']
        carrera_nombre = data['ingenieria']
        reticula = data['reticula']

        # Iniciar transacción
        cur = db.connection.cursor()

        # Insertar carrera
        cur.execute("INSERT INTO carrera (id, nombre) VALUES (%s, %s)", (carrera_id, carrera_nombre))

        # Insertar materias en la retícula
        for materia in reticula:
            cur.execute("INSERT INTO reticula (carrera_id, clave, nombre, creditos, semestre) VALUES (%s, %s, %s, %s, %s)", 
                        (carrera_id, materia['clave'], materia['nombre'], materia['creditos'], materia['semestre']))

        # Confirmar transacción
        db.connection.commit()
        cur.close()

        return jsonify({"message": "Datos insertados correctamente."}), 200

    except Exception as e:
        # Si hay un error, se revierte la transacción
        db.connection.rollback()
        return jsonify({"error": str(e)}), 500
    
#--Views--
@app.route('/index')
def index():
    return render_template('Index.html')

#Levanta el servidor con un puerto especifico
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)
