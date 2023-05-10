from random import randint
a = randint(1, 100)
_try = 10
count = 0
print('Угадай число от 1 до 100. Количество попыток: ', _try)
for i in range(_try):
    number = int(input('Введите число:'))
    count += 1
    _try -= 1
    if number == a:
        print('Угадал! У тебя ушло попыток: ', count)
        break
    else:
        if _try != 0:
            print('Попробуй ещё раз. Оставшихся попыток:', _try)
        else:
            print('Не угадал! Я не рекомендую тебе посещать казино')
