def numbers_reverse(numbers):
    j = 1
    for (i) in range(len(numbers) // 2):
        buffer = numbers[i]
        numbers[i] = numbers[i - j]
        numbers[i - j] = buffer
        j += 2
    print(numbers)


numbers_reverse([23, 71, 15, 46, 53, 16, 13, 99, 100, 120, 34.1])
