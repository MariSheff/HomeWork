'''
Задача №111327. Числа могут быть где угодно
Во входном файле записано два целых числа, которые могут быть разделены пробелами и концами строк.
Выведите в выходной файл их сумму.
Указание. Считайте весь файл в строковую переменную при помощи метода read()
и разбейте ее на части при помощи метода split().
'''
with open('Text_in.txt', 'r') as file_in:
    list = file_in.read().split()
    result = sum(map(int, list))
    print(result)

with open('Text_out.txt', 'w') as file_out:
    file_out.write(f'{int(list[0])} + {int(list[1])} = {result}')


'''
Задача №111328. Обращение строки
Во входном файле записана одна текстовая строка, возможно, содержащая пробелы.
Выведите эту строку в обратном порядке.
Строка во входном файле заканчивается символом конца строки '\n'.
'''

with open('text1.txt', 'r') as f:
    str = f.readline()[::-1]
    print(str)

'''
Задача №111329. Построчное обращение
Выведите все строки данного файла в обратном порядке.
Для этого считайте список всех строк при помощи метода readlines().
Последняя строка входного файла обязательно заканчивается символом '\n'.
'''

with open('Stroki.txt', 'r') as f:
    read_line = f.readlines()[::-1]
    for line in read_line:
        symbol = '\n'
        line = line.strip(symbol)
        print(line)


'''
Задача №111335. Статистика по файлу
Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
Выведите три найденных числа в формате, приведенном в примере.
Для экономии памяти читайте файл посимвольно,
то есть не сохраняя целиком в памяти файл или отдельные его строки.
'''

lines = 0
words = 0
symbols = 0
letters = 0
with open('Stroki.txt', 'r') as file:
    for line in file:
        for i in line:
            if i.isalpha():
                letters += 1
        lines += 1
        words += len(line.split())   #len - длина, split - разделить по пробелу
        symbols += len(line.strip('\n')) #strip - удаление начального и конечного символа, таких как перевод строки и пробел


print("Symbols:", symbols)
print("Lines:", lines)
print("Words:", words)
print("letters:", letters)

# letters1 = 0
# words1 = 0
# lines1 = 0
# with open('Stroki.txt', 'r') as f:
#     for i in f.read():
#         if i.isalpha():
#             letters += 1
#         elif i == ' ' or i == '\n':
#             words += 1
#         else:
#             lines1 += 1
#
# print(f'{letters} letters')
# print(f'{words+1} words')
# print(f'{lines1} lines')