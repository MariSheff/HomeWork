
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = int(input('Enter d: '))
e = int(input('Enter e: '))

lis = [a, b, c, d, e]

min_num = lis[0]
for el in lis:
    if el < min_num:
        min_num = el

print(min_num)
