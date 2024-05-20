
-- Consulta JSON
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
		FROM dbtec.reticula r
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
							dbtec.materias m , dbtec.especialidades e
						WHERE m.especialidad_id = e.id)
					))
		FROM 
			dbtec.especialidades e 
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
		FROM dbtec.reticula r
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
							dbtec.materias m
						WHERE m.especialidad_id = e.id) -- Filtro por el id de la especialidad actual
					))
		FROM 
			dbtec.especialidades e 
		WHERE e.carrera_id = c.id
    )
)
 AS dato
 FROM carrera c
 WHERE c.id = 4;
 
 -- datos reticula

SELECT
	json_arrayagg(json_object('id',r.id,'clave',r.clave,'nombre',r.nombre,'creditos',r.creditos,'semestre',r.semestre))
	FROM dbtec.reticula r
WHERE r.carrera_id = 1;

-- datos especialidades

SELECT 
	json_arrayagg(json_object('id',e.id,'nombre',e.name,'MateriaId',m.id,'MateriaName',m.nombre,'MateriaSmstr',m.Semestre,'MateriaCrd',m.creditos))
	FROM 
		dbtec.especialidades e
			INNER JOIN dbtec.materias m
            ON m.especialidad_id = e.id
WHERE e.carrera_id = 1;


SELECT * FROM dbtec.especialidades e;



