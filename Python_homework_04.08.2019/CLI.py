# 1. как кодом на Python вывести на экран текущую версию Python
# 2. как узнать время создания
# файла и его размер
# 3. Как убедиться, что по указанному
# пути существует директория (папка) и как вынести на экран список её содержимого


import click
import subprocess


# Alarm!!! Be very careful with parameters/arguments and options in terminal!
# Otherwise you have a risk to kill all evening to learn docs and find mistake
# that WAS NOT!!!
# However I'm master of click!

@click.group()
def info():
    pass


@info.command()
def python_version():
    subprocess.run(["python", "--version"])


@info.command()
@click.argument('file_name')
def size(file_name):
    subprocess.run('du -h ' + file_name, shell=True)


@info.command()
@click.argument('file_name')
def time(file_name):
    subprocess.run('ls -la ' + file_name, shell=True)

# Утилита test для проверки наличия файлов/директорий - true(0), false(1)
@info.command()
@click.argument('file_name')
def find(file_name):
    result = subprocess.run('test -e ' + file_name, shell=True)
    if result.returncode == 1:
        print(f"{file_name} отсутствует!")
    else:
        subprocess.run('ls -al ' + file_name, shell=True)


if __name__ == '__main__':
    info()
