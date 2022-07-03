drink_type = input()
sugar = input()
drinks_count = int(input())

total_sum = drinks_count

if drink_type == 'Espresso':
    if sugar == 'Without':
        total_sum *= 0.90 * 0.65
    elif sugar == 'Normal':
        total_sum *= 1.00
    elif sugar == 'Extra':
        total_sum *= 1.20

    if drinks_count >= 5:
        total_sum *= 0.75

elif drink_type == 'Cappuccino':
    if sugar == 'Without':
        total_sum *= 1.00 * 0.65
    elif sugar == 'Normal':
        total_sum *= 1.20
    elif sugar == 'Extra':
        total_sum *= 1.60

elif drink_type == 'Tea':
    if sugar == 'Without':
        total_sum *= 0.50 * 0.65
    elif sugar == 'Normal':
        total_sum *= 0.60
    elif sugar == 'Extra':
        total_sum *= 0.70

if total_sum > 15:
    total_sum *= 0.80

print(f'You bought {drinks_count} cups of {drink_type} for {total_sum:.2f} lv.')