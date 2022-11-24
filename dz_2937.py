
num = (int(input('Enter number:')))
print('The next number for the number ' + str(num) + ' is ' + str(num + 1))
print(f'The previous number for the number {num} is {num - 1}')


# с проверкой
num = abs(int(input('Enter number:')))
x=True
while x:
    if num < 10000:
        print('The next number for the number ' + str(num) + ' is ' + str(num + 1))
        print(f'The previous number for the number {num} is {num - 1}')
        x = False
    else:
        num = abs(int(input('Enter number:')))