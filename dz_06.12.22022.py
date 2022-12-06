'''
Задача №3450. Квадрат числа.
Число 179 записали 50 раз подряд. Полученное 150-значное число возвели в квадрат. Сколько получилось?
'''
# print(int('179'*50)**2)

'''
Задача №3458. Дележ яблок - 1
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
Входные данные
Программа получает на вход числа n и k - целые, положительные, не превышают 10000.
Выходные данные 3, 14
Выведите ответ на задачу.
'''

# n = int(input('Количество школьников:'))
# k = int(input('Количество яблок:'))
#
# print(f'Каждый школьник получит {k//n} яблок(а)')

'''
Задача №3507. Сколько совпадает чисел
Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 
3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
Входные данные
Вводятся три целых числа.
Выходные данные
Выведите ответ на задачу.
'''

# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
#
# if a == b== c:
#     print(3)
# elif a==b or b == c or a == c:
#     print(2)
# else:
#     print(0)

''' симметричное число'''
# ???????

'''
Задача №3739. Первое и последнее вхождение
Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс. 
Если она встречается два и более раз, выведите индекс её первого и последнего появления. 
Если буква f в данной строке не встречается, ничего не выводите.
При решении этой задачи нельзя использовать метод count и циклы.

Входные данные
Вводится строка.
Выходные данные
Выведите ответ на задачу.
'''

# str = input('Введите текст:')
# a = str.find('f')
# b = str.rfind('f')
# if a == -1:
#     print()
# elif a == b:
#     print(a)
# else:
#     print(a, b)

'''
Задача №3741. Удаление фрагмента
Дана строка, в которой буква h встречается минимум два раза. 
Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.
'''
# s = 'In the hole in the ground there lived a hobbit'
# print(s[0:s.find('h')] + s[s.rfind('h')+1:])



'''
Дан текст в котором встречаются имена и следующие за ними фамилии. 
Нужно получить список фамилий (last name) людей которых зовут Иван. Если на английском, то Michael)

const inputText = "Michael, how are you? - Cool, how is John Williamns and Michael Jordan? 
I don't know but Michael Johnson is fine. Michael do you still score points with LeBron James, 
Michael Green AKA Star and Michael Wood?"

Должно выдать ["Jordan", "Johnson", "Green", "Wood"]
'''

# import re
# s = 'Michael, how are you? - Cool, how is John Williamns and Michael Jordan? I don\'t know but Michael Johnson is fine. Michael do you still score points with LeBron James, Michael Green AKA Star and Michael Wood?'
#
# name = r"[Michael]+,?\s+"
# last_name = r"[A-Z][a-z]+"
# persons = re.findall(name + last_name, s)
# print(persons)
# for item in persons:
#     print(item)



'''
Написать RE которая мэтчит адреса эл. почты только с конкретным именем домена (testdomain): 
 ****@testdomain.com - valid
 ****@anotherdomain.com - not valid
'''
import re

s = 'mar@anotherdomain.com, secretary@testdomain.com, ofice@testdomain.com'
# try:
#     print('Valid' if re.findall(r'(\S*(testdomain)\b)', s)[1][1] == 'testdomain' else 'Not valid')
# except:
#     print('Not valid')

# или:
emails = re.findall(r'(\S*(testdomain.com)\b)', s)
print(emails)
n=0
for i in emails:
    print(i)
    print(emails[-n][-n])
    if emails[n][n] == 'testdomain.com':
        print('valid')
        n += 1
    else:
        print('not valid')

'''
RE для определения, есть ли в строке хотя бы одна дата в формате [mm-dd].
Две цифры для месяца, тире и две цифры для дня. Окружены квадратными скобками.) 
Работаем только с невисокосными годами. Число дней в месяцах учитывается!

1. January - 31 days
2. February - 28 days (leap years are ignored)
3. March - 31 days
4. April - 30 days
5. May - 31 days
6. June - 30 days
7. July - 31 days
8. August - 31 days
9. September - 30 days
10. October - 31 days
11. November - 30 days
12. December - 31 days

Примеры работы:

"[01-23]" // January 23rd is a valid date
"[02-31]" // February 31st is an invalid date
"[02-16]" // valid
"[ 6-03]" // invalid format
"ignored [08-11] ignored" // valid
"[3] [12-04] [09-tenth]" // December 4th is a valid date
'''