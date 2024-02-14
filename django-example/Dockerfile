# Select the python image
FROM python:3.10

# Select the work directory
WORKDIR /app

# Copy the project files
COPY requirements.txt /app/
COPY django-project /app/django-project

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Select the listening port
EXPOSE 8000

# Set the project execution command
# In this case, ENTRYPOINT is used to set the base of the command while CMD complements the base command.
# This difference is very important because, in this case, the final command will be "python django-project/manage.py runserver 0.0.0.0:8000".
# Also, consider that the CMD part can be replaced when running the docker container, but ENTRYPOINT part don't.
ENTRYPOINT ["python", "django-project/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]