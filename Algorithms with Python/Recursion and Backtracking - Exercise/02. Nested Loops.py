def print_iteration(numbers, index):
    if index == len(numbers):
        print(*numbers)
        return
    for i in range(1, len(numbers) + 1):
        numbers[index] = i
        print_iteration(numbers, index + 1)


n = int(input())
numbers = [1] * n

print_iteration(numbers, 0)
