from random import randint

class field():
    def __init__(self):
        self.field = [['О' for col in range(6)] for row in range(6)]

    def getItem(self, x, y):
        return self.field[x][y]

    def setItem(self, a, b, value):
        self.field[a][b] = value


# class ship_1():
#     def __init__(self):
#         self.data = "■"

def show_field_user(f):
    print(" ", "| 1 |", "2 |", "3 |", "4 |", "5 |", "6 |")
    j = 0
    for i in f.field:
        j += 1
        print(str(j) + ' | ' + ' | '.join(map(str, i)) + ' |')

# формируем доски компьютера и игрока

field_computer = field()
field_computer_to_show = field()
field_user = field()

# расстановка 1ого трехпалубного корабля

def ship3(f):
    n = randint(0, 1)
    if n > 0:
        y = randint(0, 3)
        x = randint(0, 5)
        f.setItem(x, y, "■"), f.setItem(x, (y + 1), "■"), f.setItem(x, (y + 2), "■")
    else:
        y = randint(0, 5)
        x = randint(0, 3)
        f.setItem(x, y, "■"), f.setItem((x + 1), y, "■"), f.setItem((x + 2), y, "■")

# расстановка 4-х однопалубных кораблей

def ship1(f):
    i = 1
    while i <= 4:
        y = randint(0, 5)
        x = randint(0, 5)
        if x >= 5:
            a = 5
        else:
            a = x + 1
        if y >= 5:
            b = 5
        else:
            b = y + 1
        if x >= 1:
            c = x - 1
        else:
            c = x
        if y >= 1:
            d = y - 1
        else:
            d = y
        if f.getItem(x, y) != '■' and f.getItem(c, y) != '■' and f.getItem(a, y) != '■' and f.getItem(x,
                                                                                                      d) != '■' and f.getItem(
                x, b) != '■':
            f.setItem(x, y, "■")
            i = i + 1

        else:
            continue

# расстановка 2-х двухпалубных кораблей

def ship2(f):
    n = 1
    while n < 3:
        y = randint(0, 5)
        x = randint(0, 5)
        a = x + 1
        b = y + 1
        c = x - 1
        d = y - 1
        e = y + 2
        g = x + 2
        if e > 5:
            e = 5
        if g > 5:
            g = 5
        if x < 5 and y < 5 and f.getItem(x, y) != '■' and f.getItem(c, y) != '■' and f.getItem(a,
                                                                                               y) != '■' and f.getItem(
                x, d) != '■' and f.getItem(x, b) != '■' and f.getItem(c, b) != '■' and f.getItem(a,
                                                                                                 b) != '■' and f.getItem(
                x, e) != '■':
            f.setItem(x, y, "■")
            f.setItem(x, b, "■")
            n = n + 1

        elif x < 5 and y < 5 and f.getItem(x, y) != "■" and f.getItem(c, y) != "■" and f.getItem(a,
                                                                                                 y) != "■" and f.getItem(
                x, d) != "■" and f.getItem(x, b) != "■" and f.getItem(a, d) != "■" and f.getItem(a,
                                                                                                 y) != "■" and f.getItem(
                a, b) != "■" and f.getItem(g, y) != "■":
            f.setItem(x, y, "■")
            f.setItem(a, y, "■")
            n = n + 1

        elif x >= 5 and y < 4 and f.getItem(x, y) != "■" and f.getItem(x, (y + 1)) != "■" and f.getItem(x, (
                y + 2)) != "■" and f.getItem((x - 1), y) != "■" and f.getItem((x - 1), (y + 1)) != "■":
            f.setItem(x, y, "■")
            f.setItem(x, (y + 1), "■")
            n = n + 1

        elif y >= 5 and x < 4 and f.getItem(x, y) != "■" and f.getItem(x - 1, y) != "■" and f.getItem((x + 1),
                                                                                                      y) != "■" and f.getItem(
                (x + 2), y) != "■" and f.getItem(x, (y - 1)) != "■" and f.getItem((x + 1), (y - 1)) != "■":
            f.setItem(x, y, "■")
            f.setItem((x + 1), y, "■")
            n = n + 1

# расставляем корабли
ship3(field_computer)
ship1(field_computer)
ship2(field_computer)
ship3(field_user)
ship1(field_user)
ship2(field_user)

# ход компьютера
def hod_computer(f):
    while True:
        x = randint(0, 5)
        y = randint(0, 5)
        if f.getItem(x, y) == 'О':
            f.setItem(x, y, "T")
            break
        if f.getItem(x, y) == '■':
            f.setItem(x, y, "X")
            break
        else:
            continue

# ход игрока

def hod_user(f):
            while True:
                place = input("Введи координаты от 1 до 6, куда стрелять, через пробел").split()
                if len(place)!=2:
                    print("Введите две координаты")
                    continue
                if not(place[0].isdigit() and place[1].isdigit()):
                    print("Введите числа")
                    continue
                a,b = map(int, place)
                if a and b not in range(1, 7):
                    print("Введите правильные координаты из диапазона от 1 до 6")
                    continue
                x=a-1
                y=b-1
                if f.getItem(x, y) == 'О':
                    f.setItem(x, y, "T")
                    field_computer_to_show.setItem(x, y, "T")
                    break
                if f.getItem(x, y) == '■':
                    f.setItem(x, y, "X")
                    field_computer_to_show.setItem(x, y, "X")
                    break
                else:
                    print("Вы уже стреляли в данные координаты")
                    continue

def proverka(f):
         if '■' in str(f.field):
             return True
         else:
            return False

print("Привет! Это игра Морской БОЙ, твои корабли мы расставили за тебя. Твоя задача победить компьютера! Удачи!!")
print("Расположение твоих кораблей")
show_field_user(field_user)

print("Расположение кораблей компьютера")
show_field_user(field_computer_to_show)

q=0
while True:
    q=q+1
    print("Ход №",q)
    hod_user(field_computer)
    print("Поле компьютера")
    show_field_user(field_computer_to_show)
    hod_computer(field_user)
    print("Поле пользователя")
    show_field_user(field_user)
    if proverka(field_computer)==False:
        print("!!!!ТЫ ПОБЕДИЛ!!!!!")
        break
    elif proverka(field_user)==False:
        print("!!!__ИИ умнее тебя___!!!")
        break
    else:
        continue
