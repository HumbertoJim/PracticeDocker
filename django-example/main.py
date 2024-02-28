import subprocess

subprocess.call(['powershell.exe', '-Command','python', 'app/manage.py', 'runserver'], shell=True)
