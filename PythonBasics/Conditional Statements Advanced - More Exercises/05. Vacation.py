budget = float(input())
season = input()
location = ''
place = ''
price = 0

summer = 'Summer'
winter = 'Winter'
alaska = 'Alaska'
morocco = 'Morocco'
hotel = 'Hotel'
hut = 'Hut'
camp = 'Camp'

if budget <= 1000:
    place = camp
    if season == summer:
        location = alaska
        price = budget * 0.65
    else:
        location = morocco
        price = budget * 0.45
elif budget <= 3000:
    place = hut
    if season == summer:
        location = alaska
        price = budget * 0.80
    else:
        location = morocco
        price = budget * 0.60
else:
    place = hotel
    price = budget * 0.90
    if season == summer:
        location = alaska
    else:
        location = morocco

print(f'{location} - {place} - {price:.2f}')