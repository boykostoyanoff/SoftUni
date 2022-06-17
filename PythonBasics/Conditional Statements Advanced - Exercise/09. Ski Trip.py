room_for_one_price = 18.00
apartment_price = 25.00
president_apartment_price = 35.00
discount = 0

days = int(input())
room_type = input()
grade = input()
room_price = 0

if room_type == 'apartment':
    room_price = apartment_price * (days - 1)
    if days < 10:
        room_price *= 0.7
    elif days <= 15:
        room_price *= 0.65
    elif days > 15:
        room_price *= 0.5
elif room_type == 'president apartment':
    room_price = president_apartment_price * (days - 1)
    if days < 10:
        room_price *= 0.9
    elif days <= 15:
        room_price *= 0.85
    elif days > 15:
        room_price *= 0.8
else:
    room_price = room_for_one_price * (days - 1)

if grade == 'positive':
    room_price *= 1.25
else:
    room_price *= 0.9

print(f'{room_price:.2f}')
