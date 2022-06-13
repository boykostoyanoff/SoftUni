rent_spring = 3000
rent_summer_autumn = 4200
rent_winter = 2600
discount = 1

budget = int(input())
season_type = input()
fisherman_count = int(input())

if fisherman_count <= 6:
    discount -= 0.1
elif fisherman_count <= 11:
    discount -= 0.15
elif fisherman_count > 11:
    discount -= 0.25

price = 0

if season_type == 'Spring':
    price = rent_spring
elif season_type == 'Summer' or season_type == 'Autumn':
    price = rent_summer_autumn
elif season_type == 'Winter':
    price = rent_winter

if fisherman_count % 2 == 0 and not season_type == 'Autumn':
    discount *= 0.95

price *= discount

if budget >= price:
    print(f'Yes! You have {(budget - price):.2f} leva left.')
else:
    print(f'Not enough money! You need {(price - budget):.2f} leva.')