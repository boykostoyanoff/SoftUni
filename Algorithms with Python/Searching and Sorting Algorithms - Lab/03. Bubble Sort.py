def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


numbers = [int(n) for n in input().split(' ')]
bubble_sort(numbers)
print(*numbers, sep=' ')
