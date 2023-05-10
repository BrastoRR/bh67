number1 = int(input('Введите первое число: '))
action = input('Укажите действие: ')
number2 = int(input('Введите второе число: '))

if number2 == 0 and action == '/':
    print('Ошибка: "Деление на ноль"')

if action == '+':
    result = number1 + number2
elif action == '-':
    result = number1 - number2
elif action == '*':
    result = number1 * number2
elif action == '/':
    result = number1 / number2
else:
    print('Ошибка: "Деление на ноль"')

print('Результат: ', result)
