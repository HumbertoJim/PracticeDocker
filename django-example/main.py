import subprocess

subprocess.call(['powershell.exe', '-Command','python', 'django-project/manage.py', 'runserver'], shell=True)
