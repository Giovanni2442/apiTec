/*--Datadase Tec--*/

use  dbtec;
delete dbtec; 
create database dbtec;

CREATE TABLE carrera(
	id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

/*reticula normalizar*/
CREATE TABLE reticula (
	id INT PRIMARY KEY,
    carrera_id INT,
    clave VARCHAR(25),
    nombre VARCHAR(255),
    creditos INT,
    semestre INT,
    FOREIGN KEY (carrera_id) REFERENCES carrera(id) ON DELETE CASCADE   -- Al eliminar un id relaciónado de la tabla carrera, se elimina el dato en reticula
);

drop table especialidades;
drop table carrera;
drop table reticula;
drop table materias;

/*especialidades normalizar*/
CREATE TABLE especialidades (
	id INT PRIMARY KEY,
	carrera_id INT,  	#tabla carrera
    name VARCHAR(255),
    FOREIGN KEY (carrera_id) REFERENCES carrera(id) ON DELETE CASCADE
);

	CREATE TABLE materias (
		id INT PRIMARY KEY,
        especialidad_id INT,
		clave VARCHAR(25),
		nombre VARCHAR(25),
		semestre INT,
		creditos INT,
        FOREIGN KEY (especialidad_id) REFERENCES especialidades(id) ON DELETE CASCADE
	);
    
    
delete from materias where id = 1;
    
-- Inserción de Datos
INSERT INTO especialidades (id,carrera_id,name) VALUES (1,1,'Redes Emergentes');
INSERT INTO especialidades (id,carrera_id,name) VALUES (2,1,'Desarrollo de Aplicaciónes Moviles');


INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (1,1,'ACF0901','robotica_II',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (2,2,'BCF0901','MATES',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (3,1,'DCF0901','DISCURSOS',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (4,1,'CCF0901','GEOGRAFIA',5,5);
INSERT INTO materias (id,especialidad_id,clave,nombre,semestre,creditos) VALUES (5,1,'DCF0901','jejeje',5,5);