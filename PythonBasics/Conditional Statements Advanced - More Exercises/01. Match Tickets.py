vip_price = 499.99
normal_price = 249.99
transport_price = 0

budget = float(input())
category = input()
people = int(input())

if 1 <= people <= 4:
    transport_price = budget * 0.75
elif 5 <= people <= 9:
    transport_price = budget * 0.6
elif 10 <= people <= 24:
    transport_price = budget * 0.50
elif 25 <= people <= 49:
    transport_price = budget * 0.4
elif 50 <= budget:
    transport_price = budget * 0.25

money_left = budget - transport_price
money_for_tickets = 0

if category == 'VIP':
    money_for_tickets = people * vip_price
else:
    money_for_tickets = people * normal_price

diff = money_left - money_for_tickets
if diff < 0:
    print(f'Not enough money! You need {abs(diff):.2f} leva.')
else:
    print(f'Yes! You have {diff:.2f} leva left.')