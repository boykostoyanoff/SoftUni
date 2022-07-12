def selection_sort(numbers):
    for step in range(len(numbers)):
        for i in range(step + 1, len(numbers)):
            if numbers[i] < numbers[step]:
                numbers[i], numbers[step] = numbers[step], numbers[i]

    print(' '.join([str(n) for n in numbers]))


data = [int(n) for n in input().split(' ')]
selection_sort(data)
