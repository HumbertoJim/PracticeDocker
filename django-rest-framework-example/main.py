import subprocess

subprocess.call(['powershell.exe', '-Command','python', 'django-rest-framework-project/manage.py', 'runserver'], shell=True)
