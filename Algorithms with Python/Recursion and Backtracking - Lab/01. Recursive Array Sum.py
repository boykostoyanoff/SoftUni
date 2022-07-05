def calc_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    return numbers.pop() + calc_sum(numbers)


numbers_list = [int(x) for x in list(input().split(' '))]
print(calc_sum(numbers_list))