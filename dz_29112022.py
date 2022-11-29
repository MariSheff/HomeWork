
# №3790. Минимум 4 чисел
'''Напишите функцию min4(a, b, c, d), вычисляющую минимум четырех чисел, которая не содержит инструкции if, а использует стандартную функцию min. Считайте четыре целых числа и выведите их минимум.
Входные данные
Вводятся четыре целых числа.
Выходные данные
Выведите ответ на задачу.
'''

def min4(*args):
    return min(args)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

print(min4(a, b, c, d))

# №3791. Длина отрезка
'''Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
Входные данные
Вводятся четыре действительных числа.
Выходные данные
Выведите ответ на задачу
'''

def distance(x1, y1, x2, y2):
    return((x1-x2)**2+(y1-y2)**2)**0.5

x1 = float(input('x1:'))
y1 = float(input('y1:'))
x2 = float(input('x2:'))
y2 = float(input('y2:'))

print(distance(x1, y1, x2, y2))


def IsPointInArea(x, y):
    return (y <= 2*x+2)*(y <= -x)*((x+1)**2*(y-1)**2 >= 4) + (y >= 2*x+2)*(y >= -x)*((x+1)**2*(y-1)**2 <= 4)

x=int(input("Введите координату X точки: "))
y=int(input("Введите координату Y точки: "))

if IsPointInArea(x, y) == 1:
    print("YES!")
else:
    print("NO")

# №3795. Принадлежит ли точка области

def IsPointInArea(x, y):
    func1 = (y >= 2 * x + 2 and y >= -1 * x and (abs((x + 1)) ** 2 + abs((y - 1)) ** 2)**0.5 <= 4)  # принадлежит кругу
    func2 = (y <= 2 * x + 2 and y <= -1 * x and not ((abs((x + 1)) ** 2 + abs((y - 1)) ** 2)**0.5 <= 4))  # не принадлежит кругу
    print(func1, func2)
    return func1 or func2

x = float(input('x:'))
y = float(input('y:'))
if IsPointInArea(x, y):
    print("YES")
else:
    print("NO")

