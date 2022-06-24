salary = 0

season = input()
destination = float(input())

if season in ['Spring', 'Autumn']:
    if destination <= 5000:
        salary = destination * 0.75
    elif destination <= 10000:
        salary = destination * 0.95
    else:
        salary = destination * 1.45
elif season == 'Summer':
    if destination <= 5000:
        salary = destination * 0.90
    elif destination <= 10000:
        salary = destination * 1.10
    else:
        salary = destination * 1.45
else:
    if destination <= 5000:
        salary = destination * 1.05
    elif destination <= 10000:
        salary = destination * 1.25
    else:
        salary = destination * 1.45
salary = salary * 4 * 0.9

print(f'{salary:.2f}')