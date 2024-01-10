# PracticeDocker
 
## Principales comandos de Docker
 * Crear tu imagen
    * **docker build -t [the name that you wnat for your image] [the path where Dockerfile is located]**
 * Muestra las imagenes creadas
    * **docker image ls**
 * Crea tu contenedor, la instancia de tu imagen (pueden haber varios contenedores a partir de una misma imagen).
    * **docker run --name [the name that you want for your container] [your image name]**
 * Muestra tus contenedores creados
    * **docker ps -a**
 * Elimina tu contenedor
    * **docker rm [your container name]**
 * Elimina tu imagen (no puedes eliminar una imagen si tienes contenedores que fueron instanciados de él)
    * **docker image rm [your image name]**

## Comandos más avanzados
 * Correr un servidor de django en segundo plano
    * **docker run -d -p [the port on your computer to use]:[the container port, the port where your application is listening] --name [container name] [image name]**
 * Detener un contenedor ejecutado en segundo plano
    * **docker stop [container name]**


## Tutorials
 * [Guía de docker para principiantes, cómo crear tu primera aplicación docker](https://www.freecodecamp.org/espanol/news/guia-de-docker-para-principiantes-como-crear-tu-primera-aplicacion-docker/)
 * [Docker python django tutorial. Dockerize a Python django App in 3 minutes](https://dockerize.io/guides/python-django-guide)