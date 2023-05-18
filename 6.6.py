def numbers_sort(numbers):
    i = 1
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            j = 1
            while numbers[i-j] % 2 != 0 and i > 0:
                buffer = numbers[i-j]
                numbers[i-j] = numbers[i]
                numbers[i] = buffer
                i -= 1
    return numbers


print(numbers_sort([5, 34, 13, 12, 11, 45, 76, 1, 90, 103, 4, 6, 1]))
