budget = float(input())
nights = int(input())
price_per_night = float(input())
percentage_costs = int(input())

nights_cost = nights * price_per_night

if nights > 7:
    nights_cost *= 0.95

other_costs = budget * percentage_costs / 100

diff = budget - nights_cost - other_costs

if diff >= 0:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    diff *= -1
    print(f"{diff:.2f} leva needed.")