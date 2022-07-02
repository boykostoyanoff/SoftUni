start = int(input())
end = int(input())
magic_number = int(input())
is_combination = False
combination_count = 0

for first_number in range(start, end + 1):
    if is_combination:
        break
    for second_number in range(start, end + 1):
        combination_count += 1
        if first_number + second_number == magic_number:
            is_combination = True
            print(f'Combination N:{combination_count} ({first_number} + {second_number} = {magic_number})')
            break

if not is_combination:
    print(f"{combination_count} combinations - neither equals {magic_number}")