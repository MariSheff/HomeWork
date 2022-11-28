# a = "\x3cdiv\x3e"
# print(a)
#
# dct = dict((("1", 1), ("2", 2), ("3", 3)))
# print(dct)
#
# matrix = [[1, 2, 3, 4, 5],
#           [2, 4, 6, 8, 9],
#           [3, 6, 9, 12, 15],
#           [4, 8, 12, 16, 20],
#           [5, 10, 15, 20, 25]]
# print(matrix[0])
# print(matrix[1][2])
# print(matrix[3][4])
#
# a = b"\x3cdiv\x3e"
# a.decode('ascii')
# print(a)
# b = "a".encode('ascii')
# print(b)
# b.decode('ascii')
# print(a)

# my_list = [1, 2, 3]
# print(my_list**2)
#
# print("First for")
# for index in range(5):
#     print(index, end=" ")
# print("\nSecond for")
# for index in range(2, 5):
#     print(index, end=" ")
# print("\nThird for")
# for index in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]:
#     print(index,end=" ")
# print("\nEnd")


# ls = list(range(0, 100, 13))
# print(ls)
#
# lst = [5, 8, 1, 3, 4]
# for index in range(len(lst)):
#     print(f"Index: {str(index)}; Element: {lst[index]}")

# lst = [5, 8, 1, 3, 4]
# for element in lst:
#     if element == 1:
#         break
#     print(element)
# else:
#     print("Оператор break не был вызван")

# lst = [5, 8, 2, 3, 4]
# for element in lst:
#     if element == 1:
#         break
#     print(element)
# else:
#     print("Оператор break не был вызван")
#
# while True:
#     answer = input()
#     if answer == "exit":
#         break
#     print(answer)

# lst = [5, 8, 1, 3, 4]
# for element in lst:
#     if element == 8 or element == 4:
#         continue
#     print(element)

#  бесконечный цикл
# count = 10
# while count > 0:
#     print(count)
#     if count == 8 or count == 4:
#         continue
#     count -= 1

# my_list = [0, 13, 26, 39]
# for idx, elem in enumerate(my_list):
#     print(idx, elem, elem**2)
#
# names = ['Bob', 'Alice', 'Guido']
# for index, value in enumerate(names, 1):
#     print(f'{index}: {value}')

# list3 = [['a', 1, 100], ['b', 2, 3], ['c', 3, 300]]
# for r, w, h in list3:
#     print(r, w, h)

# lst = []
# for el in range(2, 10, 2):
#     lst.append(el)
# print(lst)

# lst = [el for el in range(2, 100, 2)]
# print(lst)

# lst = [1, 2, 1, 3, 2, 5, 4, 3]
# st = {x for x in lst}
# print(st)
#
# keys = [1, 2, 3, 4, 5]
# dct = {key: 1 for key in keys}
# print(dct)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 8, 7, 6],
#     [5, 4, 3, 2],
# ]
# for line in matrix:
#     print("Line:", end=" ")
#     for element in line:
#         print(element, end=" ")

# a=10
# b=21
# lst=[elem for elem in range(a, b + 1) if elem % 2 == 0]
# print(lst)

# a=10
# b=21
# [print(elem, end = ' ') if elem%2 == 0 else print(0, end = " ") for elem in range(a, b + 1) ]

# [print(item, end = " ") for item in [elem if elem%2 == 0 else 0 for elem in range(a, b + 1) ]]

# for elem in range(a,b+1):
#     if elem % 2 == 0:
#         print(elem,end = " ")
#     else:
#         print(0, end=" ")

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 8, 7, 6],
#     [5, 4, 3, 2],
# ]
# lst = []
# for line in matrix:
#      lst.append(line)
# print(lst)

keys = [1, 2, 3, 4, 5]
values = [100, 200, 300, 400, 500]
dct = {key: value for key, value in zip(keys, values)}
print(dct)

n = 5
x=0
for i in range(1, n+1):
    x +=i**2
print(x)