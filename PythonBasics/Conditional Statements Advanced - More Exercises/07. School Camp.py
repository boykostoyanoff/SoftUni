season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())
sport = ''
price = 0

if season == 'Winter':
    if group_type in ['boys', 'girls']:
        price = 9.60
        if group_type == 'boys':
            sport = 'Judo'
        else:
            sport = 'Gymnastics'
    elif group_type == 'mixed':
        price = 10
        sport = 'Ski'
elif season == 'Spring':
    if group_type in ['boys', 'girls']:
        price = 7.20
        if group_type == 'boys':
            sport = 'Tennis'
        else:
            sport = 'Athletics'
    elif group_type == 'mixed':
        price = 9.50
        sport = 'Cycling'
elif season == 'Summer':
    if group_type in ['boys', 'girls']:
        price = 15
        if group_type == 'boys':
            sport = 'Football'
        else:
            sport = 'Football'
    elif group_type == 'mixed':
        price = 20
        sport = 'Swimming'

if 10 <= students_count < 20:
    price *= 0.95
elif 20 <= students_count < 50:
    price *= 0.85
elif students_count >= 50:
    price *= 0.50

price = price * nights_count * students_count

print(f'{sport} {price:.2f} lv.')