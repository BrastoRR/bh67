def sum_of_neighbours(numbers):
    result = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i - 1] + numbers[i + 1])
        else:
            result.append(numbers[i - 1] + numbers[0])
    return result


print(sum_of_neighbours([1, 2, 4, 8, 2, 3, 4, 1, 9, 0, 4, 6, 1]))
