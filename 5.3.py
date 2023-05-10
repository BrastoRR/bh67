n = int(input('Введите Nmax: '))
number = 2
data = []
counter = 0
while number <= n:
    if number % 2 == 0:
        data.append(number)
        counter += 1
    number += 1
    if counter == 5:
        print(data)
        counter = 0
        data = []
if data != 0:
    print(data)
