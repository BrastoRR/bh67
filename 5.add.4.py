cost = int(input('Укажи сумму:'))
if cost >= 1:
    if cost >= 5:
        if cost >= 10:
            if cost >= 25:
                count_25 = cost // 25
                cost = cost % 25
                print('Монеты наминалом 25, шт: ', count_25)
            count_10 = cost // 10
            cost = cost % 10
            print('Монеты наминалом 10, шт: ', count_10)
        count_5 = cost // 5
        cost = cost % 5
        print('Монеты наминалом 5, шт: ', count_5)
    count_1 = cost // 1
    print('Монеты наминалом 1, шт: ', count_1)
result = count_25 + count_10 + count_5 + count_1
print('Минимальное количестов монет: ', result)
