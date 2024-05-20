/*--Datadase Tec--*/

CREATE TABLE carrera(
	id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
use  dbtec;
create database dbtec;

/*reticula normalizar*/
CREATE TABLE reticula (
	id INT PRIMARY KEY,
    carrera_id INT,
    clave VARCHAR(25),
    nombre VARCHAR(255),
    creditos INT,
    semestre INT,
    FOREIGN KEY (carrera_id) REFERENCES carrera(id)
);

drop table especialidades;
drop table materias;

/*especialidades normalizar*/
CREATE TABLE especialidades (
	id INT PRIMARY KEY,
	carrera_id INT,  	#tabla carrera
    name VARCHAR(255),
    FOREIGN KEY (carrera_id) REFERENCES carrera(id)
);

	CREATE TABLE materias (
		id INT PRIMARY KEY,
        especialidad_id INT,
		clave VARCHAR(25),
		nombre VARCHAR(25),
		semestre INT,
		creditos INT,
        FOREIGN KEY (especialidad_id) REFERENCES especialidades(id)
	);

