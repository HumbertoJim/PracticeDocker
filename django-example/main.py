import pathlib
import subprocess
import os

BASE_DIR = pathlib.Path(__file__).parent
print(BASE_DIR)

os.chdir(BASE_DIR)

subprocess.call(['powershell.exe', '-Command','dir'], shell=True)
subprocess.call(['powershell.exe', '-Command', '.\\venv\\Scripts\\Activate.ps1'], shell=True)

os.chdir(BASE_DIR / 'django-project')
subprocess.call(['powershell.exe', '-Command','python', 'manage.py', 'runserver'], shell=True)