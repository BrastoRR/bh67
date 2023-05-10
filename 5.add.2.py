qty = int(input('Введите количество вводимых чисел: '))
numbers = list()
amount = 0
for i in range(qty):
    num = int(input('Введите число: '))
    numbers.append(num)
    amount += num
result = amount / qty
print(result)
