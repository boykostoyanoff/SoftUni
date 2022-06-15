month = input()
nights = int(input())
one_night_studio = 0
one_night_apartment = 0

if month == 'May' or month == 'October':
    one_night_studio = 50.00
    one_night_apartment = 65.00
elif month == 'June' or month == 'September':
    one_night_studio = 75.2
    one_night_apartment = 68.70
elif month == 'July' or month == 'August':
    one_night_studio = 76.00
    one_night_apartment = 77.00

studio_price = nights * one_night_studio
apartment_price = nights * one_night_apartment

if 7 < nights <= 14 and (month == 'May' or month == 'October'):
    studio_price *= 0.95
elif nights > 14:
    apartment_price *= 0.9
    if month == 'May' or month == 'October':
        studio_price *= 0.7
    elif month == 'June' or month == 'September':
        studio_price *= 0.8

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')