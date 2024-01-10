# Este script sirve para crear una imagen de docker, es un archivo que indica lo que contendra la imagen y el tipo de imagen que sera.

# Indica la imagen de docker y la version a utilizar
# Piensa en la imagen como si fuera otra computadora que tiene todas las dependencias necesarias.
# En este caso, la imagen python cuenta con las dependencias para python
FROM python:3.10

# Establece cual sera la ruta que se utilizara para ejecutar comandos en la imagen. Puedes verlo como la ruta de tu projecto.
WORKDIR /app

# Lo siguiente es mover nuestros archivos, en este caso nuestro codigo de python, a la imagen.
# Piensa en esta accion como si estuvieras moviendo el archivo de tu computadora a la computadora de docker.
# El primer parametro es la ruta de tu archivo que quieres mover, el segundo parametro es la ruta en donde se guardara.
COPY main.py /app/

# Por ultimo, se indica el comando que sera ejecutado una vez la imagen de docker sea lanzada (sinonimo de iniciar, ejecutar).
# En este caso, como se desea correr el script de main.py, lo que se indica es que se usara la aplicacion de python,
# para ejecutar el script main.py.
# Aunque tiene vista de ser una lista, piensa en que es la tipica linea de comando que se utiliza para correr
# un archivo en consola. Por ejemplo "python manage.py runserver", "python file.py", "python main.py"
CMD [ "python", "main.py" ]