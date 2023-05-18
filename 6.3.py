def numbers_shift(n):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = numbers[n + 1:] + numbers[:n + 1]
    print(numbers)

numbers_shift(5)
