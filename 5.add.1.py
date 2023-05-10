number = input('Введите число: ')
result = 0
for i in range(len(number)):
    num = int(number[i])
    if num > result:
        result = num

print('Максимальная цифра вашего числа:', result)
