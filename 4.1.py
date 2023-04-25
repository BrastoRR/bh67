n = input('Введите степень до которой следует заполнять список: ')
numbers = [2**i for i in range(int(n))]
print(numbers)
