# Давайте реализуем один из известных паттернов проектирования.
# Этим паттерном будет Компоновщик.
# Он создан для структурирования объектов, компонуя объекты в древовидные структуры.
# HTML, дерево файлов и папок в Linux - яркие примеры таких структур. Вы же создатите текстовое отображение папок
# и вложенных файлов:
# Создайте класс BaseNode, которые принимает в констукторе имя и сохраняет его у себя.
# А также имеет метод __repr__, который ничего не делает.
# Создайте класс File, который будет наследником  BaseNode. У него должен быть переопределен метод __repr__,
# который должен возвращать строку 'file: "<имя файла>"'.
# Создайте класс Dir,   который будет наследником BaseNode.
# У него должно быть хранилище вложенных в него файлов и папок.
# Должен быть метод add, добавляющий файл или папку. Должен быть метод remove, удаляющий вложенную
# в него ранее файл или папку.
# И переопределен метод __repr__, который будет возвращать строку
# 'directory: <имя папки> (<перечисление вложенных папок и файлов через запятую или слово empty, если папка пуста>).
# В итоге у Вас должен написанный ниже код работать так, как в примере.
# Внимательно изучите пример, он даст все подсказки
# (включая знание об аргуметнах, которые должны принимать методы и т. д.).
# Посмотрите примеры реализации этого паттерна, она достаточно проста на любом языке.
# Продолжение на слайде ниже.

class BaseNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass


class File(BaseNode):
    def __repr__(self):
        return 'file: "{}"'.format(self.name)


class Dir(BaseNode):
    def __init__(self, name):
        self.name = name
        self.listFileDir = list()

    def add(self, smth):
        self.listFileDir.append(smth)

    def remove(self, smth):
        self.listFileDir.remove(smth)

    def __repr__(self):
        self.s = ", ".join([str(f) for f in self.listFileDir])
        if len(self.listFileDir) < 1:
            return "directory: {} (empty)".format(self.name)
        else:
            return "directory: {} ({})".format(self.name, self.s)

    def __str__(self):
        return self.__repr__()
        if len(self.listFileDir) <= 1:
            return "directory: {} (empty)".format(self.name)
        else:
            return "directory: {} ({})".format(self.name, self.listFileDir)


d1 = Dir('dir1')
d1.add(File('text.txt'))
d2 = Dir('dir2')
d1.add(d2)
d3 = Dir('dir3')
d1.add(d3)

print(d1)
d1.remove(d3)
print(d1)
d4 = Dir('dir4')
d2.add(d4)
d4.add(File('image1.txt'))
d4.add(File('text2.txt'))
d1.add(File('paper1.pdf'))
d2.add(Dir('dir5'))

print(d1)
print(d1)

