# №3443 Вычислите 2 в степени 179. Выведите на экран вычисленное значение

print(2**179)

# №3445 Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971

c = (179**2+971**2)**(0.5)
print (c)

# №3455 Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами, округление до 10 знака
# предполагается, что треугольник прямоугольный

a = int(input('а:'))
b = int(input('b:'))
c = round((a**2+b**2)**(0.5),10)
print(c)

# №3456 Hello, Harry!

name = 'Harry'
print(f'Hello, {name}!')

# №3502. Какое число больше?

x = int(input('x:'))
y = int(input('y:'))

if x>y:
    print(x)
elif x<y:
    print(y)
else:
    print(0)


# №3503. Функция. Знак числа

def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

x = int(input('x:'))
print(sign(x))

# №3735. Делаем срезы

my_str = 'Abrakadabra'
print(my_str[2])
print(my_str[-2])
print(my_str[0:5])
print(my_str[0:-2])
print(my_str[0::2])
print(my_str[1::2])
print(my_str[::-1])
print(my_str[::-2])
print(len(my_str))

# №3736. Количество слов, метод count ???

my_st = 'Hello world'
print(len(my_st.split()))

# count
print(my_st.count(" ")+1)


