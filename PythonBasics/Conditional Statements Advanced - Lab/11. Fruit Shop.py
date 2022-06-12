fruit_name = input()
day_of_week = input()
quantity = float(input())

result = 'error'

if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit_name == 'banana':
        result = 2.50
    elif fruit_name == 'apple':
        result = 1.20
    elif fruit_name == 'orange':
        result = 0.85
    elif fruit_name == 'grapefruit':
        result = 1.45
    elif fruit_name == 'kiwi':
        result = 2.70
    elif fruit_name == 'pineapple':
        result = 5.50
    elif fruit_name == 'grapes':
        result = 3.85
elif day_of_week in ['Saturday', 'Sunday']:
    if fruit_name == 'banana':
        result = 2.70
    elif fruit_name == 'apple':
        result = 1.25
    elif fruit_name == 'orange':
        result = 0.90
    elif fruit_name == 'grapefruit':
        result = 1.60
    elif fruit_name == 'kiwi':
        result = 3.00
    elif fruit_name == 'pineapple':
        result = 5.60
    elif fruit_name == 'grapes':
        result = 4.20

if not result == 'error':
    result *= quantity
    print(f'{result:.2f}')
else:
    print(result)