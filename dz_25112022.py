# №334. Четные числа
'''Входные данные
вводятся 4 числа: a, b, c и d.
Входные данные
выведите все числа на отрезке от a до b, дающие остаток c при делении на d.
Если таких чисел не существует, то ничего выводить не нужно.
'''

a = 1
b = 12
c = 0
d = 2

[print(el, end=' ') if el % d == c else 0 for el in range(a, b + 1)]

print()
# №3642. Список квадратов
'''По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
Входные данные
Вводится натуральное число.
Выходные данные
Выведите ответ на задачу.
'''
n = 50

for i in range(n):
    x = i**2
    if x < n:
        print(x, end=' ')

print()
# №3644. Список степеней двойки
'''По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания.
Операцией возведения в степень пользоваться нельзя!
Входные данные
Вводится натуральное число.
Выходные данные
Выведите ответ на задачу
'''
n = 50
for i in range(n):
    x = pow(2, i)
    if x <= n:
        print(x, end=' ')


print()
# №3647. Утренняя пробежка
'''В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. 
По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
Входные данные
Программа получает на вход действительные числа x и y
Выходные данные
Программа должна вывести одно натуральное число.
'''
x = 10
y = 20
day = 1

while x < y:
    x += x * 0.1
    day += 1
print(day)

print()
# №3533. Факториал
'''
По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
0! = 1
Входные данные
Вводится число n.
Выходные данные
Выведите ответ на задачу.
'''
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
print(fact)

# №3535. Пингвины
n = 3
print('   _~_     '*n)
print('  (o o)    '*n)
print(' /  V  \   '*n)
print('/(  _  )\  '*n)
print('  ^^ ^^    '*n)

# №315. Сумма квадратов
n = 5
x=0
for i in range(1, n+1):
    x +=i**2
print(x)
