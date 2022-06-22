import math

x = int(input())
y = float(input())
z = int(input())
workers = int(input())

area_for_grape = x * 0.40
total_grape = area_for_grape * y
total_wine = total_grape / 2.5

if total_wine < z:
    wine_needed = z - total_wine
    print(f'It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.')
else:
    wine_left = total_wine - z
    wine_for_one_worker = wine_left / workers
    print(f'Good harvest this year! Total wine: {math.floor(total_wine)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_for_one_worker)} liters per person.')