n = int(input())
time_of_day = input()
start_sum = 0
money_per_km = 0

if n < 20:
    start_sum = 0.70
    if time_of_day == 'day':
        money_per_km = 0.79
    else:
        money_per_km = 0.9
elif n < 100:
    money_per_km = 0.09
else:
    money_per_km = 0.06

total_sum = n * money_per_km + start_sum
print(f'{total_sum:.2f}')