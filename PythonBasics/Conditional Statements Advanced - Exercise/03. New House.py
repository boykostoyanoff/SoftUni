flower_type = input()
flower_quantity = int(input())
budget = float(input())

discount = 100
flower_price = 0

if flower_type == 'Roses':
    flower_price = 5
    if flower_quantity > 80:
        discount -= 10
elif flower_type == 'Dahlias':
    flower_price = 3.80
    if flower_quantity > 90:
        discount -= 15
elif flower_type == 'Tulips':
    flower_price = 2.80
    if flower_quantity > 80:
        discount -= 15
elif flower_type == 'Narcissus':
    flower_price = 3
    if flower_quantity < 120:
        discount += 15
elif flower_type == 'Gladiolus':
    flower_price = 2.50
    if flower_quantity < 80:
        discount += 20

total_price = flower_quantity * flower_price * (discount / 100)

if budget - total_price < 0:
    print(f'Not enough money, you need {(total_price - budget):.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {flower_quantity} {flower_type} and {(budget - total_price):.2f} leva left.')