/*--Controlador de la bd--*/

-- Despliegue de tablas
use dbtec;

delete from carrera where id = 1;

SELECT * FROM carrera;
SELECT * FROM materias;
SELECT * FROM reticula;
SELECT * FROM especialidades;

/*--Insertar datos--*/
#Insertar carreras
INSERT INTO carrera(id,name) VALUES (1,'Sistemas Computaciónales');
INSERT INTO carrera(id,name) VALUES (2,'Electromecanica');
INSERT INTO carrera(id,name) VALUES (3,'Mecatrónica');
INSERT INTO carrera(id,name) VALUES (4,'Logiística');
INSERT INTO carrera(id,name) VALUES (5,'Industrial');
INSERT INTO carrera(id,name) VALUES (6,'TIC´S');
INSERT INTO carrera(id,name) VALUES (7,'Gestion Empresarial');

#Insertar Reticula
INSERT INTO reticula (id,carrera_id,clave,nombre,creditos,semestre) VALUES (1,1,'ACF0901','Calculo Diferencial',5,1);
INSERT INTO reticula (id,carrera_id,clave,nombre,creditos,semestre) VALUES (3,1,'ACF0666','Calculo Diferencial',5,2);
INSERT INTO reticula (id,carrera_id,clave,nombre,creditos,semestre) VALUES (4,1,'ACF5451','Calculo Diferencial',5,3);
INSERT INTO reticula (id,carrera_id,clave,nombre,creditos,semestre) VALUES (2,2,'BCRT944','Calculo erencial',5,1);

-- Insertar materias de Especialidad
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (1,2,'ACF0901','robotica_II',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (2,2,'ACF0901','e',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (3,2,'ACF0901','r',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (4,1,'ACF0901','g',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (5,1,'ACF0901','fefe',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (6,1,'ACF0901','tete',5,5);

-- Insertar Especialidades
INSERT INTO especialidades (id,carrera_id,name) VALUES (2,1,'Programación');
INSERT INTO especialidades (id,carrera_id,name) VALUES (1,1,'Redes Emergentes');

UPDATE especialidades SET carrera_id = 1, name = "Redes Convergentes" WHERE especialidades.id = 1;

/*--Manipular datos de la BD--*/
SELECT c.id,c.name FROM carrera c;

SELECT * FROM carrera;
SELECT * FROM reticula;
SELECT * FROM materias;
SELECT * FROM especialidades;


-- datos carrera
SELECT 
 JSON_OBJECT('id',c.id,'name',c.name)
 AS dato
 FROM carrera c
 where c.id =1;
 
 -- datos reticula
 SELECT 
	json_arrayagg(json_object('id',r.id,'clave',r.clave,'nombre',r.nombre,'creditos',r.creditos,'semestre',r.semestre))
FROM 
	dbtec.reticula r
		INNER JOIN dbtec.carrera c 
        ON c.id = r.id
        INNER JOIN 


