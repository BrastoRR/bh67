def number_convert(number):
    binary = ''
    while number > 1:
        binary = f'{number % 2}' + binary
        number //= 2
    binary = f'{number}' + binary
    to_decimal = binary[::-1]
    decimal = 0
    for i in range(len(to_decimal)):
        if to_decimal[i] == '1':
            decimal = (2 ** i) + decimal
    return binary, decimal


print(number_convert(105))