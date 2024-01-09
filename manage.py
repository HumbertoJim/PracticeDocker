import os
import sys
import subprocess


class Manager:
    def __init__(self) -> None:
        self.messages = dict(
            commands=f'Commands\n{"-"*20}\n * startproject\n * runproject\n'
        )

    def startproject(self, project):
        if os.path.exists(project) and os.path.isdir(project):
            raise Exception(f'Project {project} already exists')
        os.mkdir(project)
        files = ['main.py', 'Dockerfile', 'requirements.txt']
        for filename in files:
            file = open(f'{project}/{filename}', 'a')
            file.close()
        subprocess.call(['python', '-m', 'venv', f'{project}/venv'])
        print(f'Project {project} created')

    def runproject(self, project):
        subprocess.call(['python', f'{project}/main.py'])

    def run(self, argv):
        try:
            if len(argv) < 2:
                raise Exception(f'Command was not specified. Please check allowed commands.\n\n{self.messages["commands"]}')
            command = argv[1]
            if command  == 'startproject':
                if len(argv) < 3:
                    raise Exception('Command startproject requires the project name as parameter')
                project = argv[2]
                self.startproject(project)
            elif command == 'runproject':
                if len(argv) < 3:
                    raise Exception('Command runproject requires the project name as parameter')
                project = argv[2]
                self.runproject(project)
            else:
                raise Exception(f'Invalid command {command}. Please check allowed commands.\n\n{self.messages["commands"]}')
        except Exception as e:
            print(f'Error\n{"-"*80}\n{e}')

manager = Manager()
manager.run(sys.argv)