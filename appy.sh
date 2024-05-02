#!/bin/bash

#bahc script   : Automatiza instrucciónes en consola desde un scripting. Esto nos ayuda para la creación
#                del contenedor de manera automatica y rapida

#mkdir tempdir  #Crea una carpeta "tempdir"
#mkdir tempdir/templates
#mkdir tempdir/static

#cp app.py tempdir                         #Copiar el archivo "app.py" a  carpeta "tempdir"  
#cp requirements.txt tempdir             
#cp Dockerfile tempdir
#cp -r templates/* tempdir/templates       #mover toda una carpeta a otra
#cp -r static/* tempdir/static

cd tempdir                                # acceder a la carpeta tempdir

docker build -t app .                       #Construir la api
docker run -t -d -p 5050:3000 --name apprun app     #publicar la api desde un puerto especifico
docker ps -a            #Despliega en consola las imagenes corriendo desde docker

