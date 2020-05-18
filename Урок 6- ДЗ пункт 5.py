class Stationer:
    def draw(self, title):
        self.title = self.title
        print(f'Запуск отрисовки')


class Pen (Stationer):
    def draw (self, title):
        self.title = title
        print(f'Отрисовка {self.title}')

class Pencil (Stationer):
    def draw (self):
        self.title = 0
        print('Отрисовка карандашом')

class Handle (Stationer):
    def draw (self):
        self.title = 0
        print('Отрисовка маркером')

a =  Pen()
f = a.draw('ручка')
a =  Pencil()
f = a.draw()
a =  Handle()
f = a.draw()