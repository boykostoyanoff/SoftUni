def revere_arr(left_index, numbers):
    if left_index == len(numbers) // 2:
        return numbers
    right_index = len(numbers) - 1 - left_index
    numbers[left_index], numbers[right_index] = numbers[right_index], numbers[left_index]
    revere_arr(left_index + 1, numbers)


nums = list(input().split(' '))
revere_arr(0, nums)
print(' '.join(nums))


