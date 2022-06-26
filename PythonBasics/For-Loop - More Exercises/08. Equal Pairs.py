n = int(input())
max_diff = 0
value = 0
is_some_value = True
last_pair_sum = 0

for _ in range(n):
    first_number = int(input())
    second_number = int(input())
    sum_numbers = first_number + second_number
    if _ == 0:
        value = sum_numbers
        last_pair_sum = sum_numbers
        continue
    if not sum_numbers == value:
        is_some_value = False
        if abs(last_pair_sum - sum_numbers) > max_diff:
            max_diff = abs(last_pair_sum - sum_numbers)
        last_pair_sum = sum_numbers
if is_some_value:
    print(f'Yes, value={value}')
else:
    print(f'No, maxdiff={max_diff}')
