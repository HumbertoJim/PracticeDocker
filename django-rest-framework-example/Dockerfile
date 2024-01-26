FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
COPY django-rest-framework-project /app/django-rest-framework-project

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "django-rest-framework-project/manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]