FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
COPY app /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]