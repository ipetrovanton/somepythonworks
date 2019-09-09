# Есть класс Person, конструктор которого принимает три параметра
# (не учитывая self) – имя, фамилию и квалификацию специалиста.
# Квалификация имеет значение заданное по умолчанию, равное единице.
# У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
# Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
# (вместо троеточия должны выводиться имя и фамилия объекта).
# В основной ветке программы создайте три объекта класса Person.
# Посмотрите информацию о сотрудниках и увольте самое слабое звено.

class Person:
    def __init__(self, name, secondName, qualification=1):
        self.name = name
        self.secondName = secondName
        self.qualification = qualification

    def __del__(self):
        print("До свидания, мистер {} {}".format(self.name, self.secondName))

    def info(self):
        print("Name: {}, Second Name: {}, Qualification: {}".format(self.name, self.secondName, self.qualification))


employee1 = Person("Иван", "Иванов", 5)
employee2 = Person("Сидор", "Сидоров", 3)
employee3 = Person("Иван", "Сидоров")

print("Вы самое слабое звено - прощайте!")
del employee3

print("Конец рабочего дня:")

