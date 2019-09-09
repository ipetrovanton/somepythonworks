import time


class TestManager:

    def __enter__(self):
        print('Сейчас начнется код внутри менеджера')
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timer = time.time() - self.start
        print('Код выполнился. Время выполнения - {}'.format(self.timer))


with TestManager():
    a = 1 << 10000000
    s = str(a)
    print(s)
    print(len(s))
