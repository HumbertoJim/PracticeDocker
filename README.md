# Practice Docker

## Docker
### Example
```
# Docker image with specific version.
FROM python:3.10

# Directory where commands will be executed.
WORKDIR /usr/src/app

# Declare Env variables.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# Copy folders and files from the host to the image.
COPY app /app/
COPY requirements.txt dest

# Run commands, in this example installing dependencies.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port 8000 so the host can access to it.
EXPOSE 8000

# Define the entrypoint command, which means that any specified command will be prefixed with the entrypoint.
ENTRYPOINT [ "python", "manage.py" ]

# Define a default command that will be executed when running the container. Unlike ENTRYPOINT, the CMD command can be replaced when running the container.
CMD [ "runserver", "0.0.0.0:8000" ]
```

### Comandos
 * Crear tu imagen
    - `docker build -t [the tag that you want for your image] [the path where Dockerfile is located]`
 * Muestra las imagenes creadas
    - `docker image ls`
 * Crea tu contenedor, la instancia de tu imagen (pueden haber varios contenedores a partir de una misma imagen).
    - `docker run --name [the name that you want for your container] [your image tag]`
 * Muestra tus contenedores creados
    - `docker ps -a`
 * Elimina tu contenedor
    - `docker rm [your container name]`
 * Elimina tu imagen (no puedes eliminar una imagen si tienes contenedores que fueron instanciados de él)
    - `docker image rm [your image tag]`

### Comandos avanzados
 * Correr un servidor de django en segundo plano
    - `docker run -d -p [the port on your computer to use]:[the container port, the port where your application is listening] --name [container name] [image tag]`
 * Detener un contenedor ejecutado en segundo plano
    - `docker stop [container name]`

## Docker-compose
### Example
```
# Specify that the yaml file uses the docker compese syntax version 3.8.
version: '3.8'

# Define a list with the services that compose your application
services:
   # Here a service called "web" is defined. You can use any name.
   web:
      # Specify the path where the Dockerfile is located. The service will  be built using that Dockerfile.
      build: ./app
      # Specify the command that will be used when running the service.
      command: python manage.py runserver 0.0.0.0:8000
      # Mount a host directory on the specified container path. This means that any local changes will be reflected on the container path.
      volumes:
         - ./app/:/usr/src/app/
      # Maps a port from the container to a port from the host. The first port corresponds to host.
      ports:
         - 8000:8000
      # Specify the .env file that will be used in your service. These is very useful when working with several .env files.
      env_file:
         - ./.env.dev
```

### Comandos
 * Crea las imagenes de tu aplicación
    - `docker-compose build`
 * Corre los contenedores de tu aplicación en segundo plano
    - `docker-compose up -d`
 * Construye las imagenes y despues crea los contenedores de tu aplicacion
    - `docker-compose up -d --build`
 * Detiene la aplicación
    - `docker compose stop`

### Comandos avanzados
 * Ejecuta un comando
    - `docker compose exec [project name, usually the foldername] [command with args]`
 * Muestra los logs de la aplicación
    - `docker compose logs -f`
 * Inspecciona un volumen
    - `docker volume inspect [project name, usually the folder name]_[volume name]`
 * Detiene la aplicación y los volúmenes asociados
    - `docker compose down -v`

## Tutorials
 * [Guía de docker para principiantes, cómo crear tu primera aplicación docker](https://www.freecodecamp.org/espanol/news/guia-de-docker-para-principiantes-como-crear-tu-primera-aplicacion-docker/)
 * [Docker python django tutorial. Dockerize a Python django App in 3 minutes](https://dockerize.io/guides/python-django-guide)
 * [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)