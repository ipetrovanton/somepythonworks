import os


class Storage:
    def __init__(self, path):
        self.path = path
        self.my_file = open(self.path, "w")
        self.my_file.close()

    def get(self):
        buf = ""
        with open(self.path, "r") as file:
            buf += file.read()
            return buf

    def add(self, data):
        with open(self.path, "a") as file:
            file.write(str(data) + "||011110LOL\nq")

    def size(self):
        return os.path.getsize(self.path)


s = Storage("СТОРОЖ.txt")
s.add("Ghbdtn!")
s.add("Привет!")
s.add("Снова Привет!")

print(s.get())
print(s.size())
