first_number = int(input())
second_number = int(input())

action = input()
result = ''

if action == '/' or action == '%':
    if second_number == 0:
        result = f'Cannot divide {first_number} by zero'
    else:
        if action == "/":
            result = first_number / second_number
            result = f'{first_number} {action} {second_number} = {result:.2f}'
        else:
            result = first_number % second_number
            result = f'{first_number} {action} {second_number} = {result}'
else:
    if action == '*':
        result = first_number * second_number
    elif action == '-':
        result = first_number - second_number
    elif action == '+':
        result = first_number + second_number
    parity = 'even' if result % 2 == 0 else 'odd'
    result = f'{first_number} {action} {second_number} = {result} - {parity}'
print(result)