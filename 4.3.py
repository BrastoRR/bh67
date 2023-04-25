from collections import *
data = defaultdict(list)
item = input('Введите количество Users для которых будут вноситься данные: ')
for i in range(int(item)):
      name = input('Введите имя: ')
      email = input('Введите email: ')
      list = {name, email}
      data[i].append(list)
print(data)
