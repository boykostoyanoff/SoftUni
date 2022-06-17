n = int(input())
min_number = int(input())
max_number = min_number

for _ in range(n-1):
    number = int(input())
    if min_number > number:
        min_number = number
    if max_number < number:
        max_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')