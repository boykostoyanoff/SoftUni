junior_cyclists = int(input())
senior_cyclists = int(input())
route_type = input()

junior_tax = 0
senior_tax = 0

if route_type == 'trail':
    junior_tax = 5.50
    senior_tax = 7
elif route_type == 'cross-country':
    junior_tax = 8
    senior_tax = 9.50
elif route_type == 'downhill':
    junior_tax = 12.25
    senior_tax = 13.75
elif route_type == 'road':
    junior_tax = 20
    senior_tax = 21.50

discount_for_50_in_cross_country = 0.25

money = junior_cyclists * junior_tax + senior_cyclists * senior_tax

if junior_cyclists + senior_cyclists >= 50 and route_type == 'cross-country':
    money -= money * discount_for_50_in_cross_country

money -= money * 0.05

print(f'{money:.2f}')