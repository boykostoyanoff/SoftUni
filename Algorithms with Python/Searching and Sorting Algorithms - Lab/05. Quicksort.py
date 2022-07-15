def quick_sort(numbers: list):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers.pop()
    left_part = []
    right_part = []

    for number in numbers:
        if number < pivot:
            left_part.append(number)
        else:
            right_part.append(number)

    return quick_sort(left_part) + [pivot] + quick_sort(right_part)


nums = quick_sort([int(x) for x in input().split(' ')])
print(*nums)