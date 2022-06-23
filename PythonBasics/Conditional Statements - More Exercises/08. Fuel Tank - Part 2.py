b = 2.22
d = 2.33
g = 0.93

b_discount = 0.18
d_discount = 0.12
g_discount = 0.08

fuel_type = input()
fuel_quantity = float(input())
has_card = input()

if has_card == 'Yes':
    b -= b_discount
    d -= d_discount
    g -= g_discount

price = 0

if fuel_type == 'Gas':
    price = g * fuel_quantity
elif fuel_type == 'Gasoline':
    price = b * fuel_quantity
else:
    price = d * fuel_quantity

if 20 <= fuel_quantity <= 25:
    price = price * 0.92
elif fuel_quantity > 25:
    price = price * 0.90

print(f'{price:.2f}')