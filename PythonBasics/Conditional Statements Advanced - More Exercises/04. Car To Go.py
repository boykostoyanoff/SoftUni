budget = float(input())
season = input()

car_class_type = ''
car_type = ''
car_price = 0

if budget <= 100:
    car_class_type = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.35
    else:
        car_type = 'Jeep'
        car_price = budget * 0.65

elif budget <= 500:
    car_class_type = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.45
    else:
        car_type = 'Jeep'
        car_price = budget * 0.80
else:
    car_class_type = 'Luxury class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.90
    else:
        car_type = 'Jeep'
        car_price = budget * 0.90

print(car_class_type)
print(f'{car_type} - {car_price:.2f}')