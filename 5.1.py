n = int(input('Введите количество чисел для вывода: '))
m = int(input('Введите число, которому они должны быть кратны: '))
k = int(input('Введите число, больше которого должны быть выводимые числа: '))
number = k + 1
counter = 0
while counter < n:
    if number % m == 0:
       print(number)
       counter += 1
    number += 1

print('finish')