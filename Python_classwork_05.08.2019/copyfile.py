import os


def copyfile(source, appointment):
    buf = ""
    try:
        with open(source, "r") as file:
            buf += file.read()
    except IOError:
        print(f"File: {source} can't be find!")

    try:
        with open(appointment, "x") as file:
            file.write(buf)
    except IOError:
        print(f"File: {appointment} was created early! Change name of destination file!")


# copyfile("len.py", "file.py")


def copydir(from_dir, to_dir):
    print(os.path.isdir(from_dir))
    print(f"Current {from_dir}")
    print(f"Destination {to_dir}")
    file_list = os.listdir(from_dir)
    os.mkdir(to_dir)
    for i in file_list:
        s = from_dir + '/' + i
        if os.path.isdir(s):
            m = to_dir + '/' + i
            copydir(s, m)
        else:
            m_file = to_dir + '/' + i
            copyfile(i, m_file)


copydir("123", "new_dir")
