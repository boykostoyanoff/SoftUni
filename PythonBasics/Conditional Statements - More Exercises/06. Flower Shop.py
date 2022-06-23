import math

m = 3.25
z = 4.00
r = 3.50
k = 8
tax = 0.05

m_quantity = int(input())
z_quantity = int(input())
r_quantity = int(input())
k_quantity = int(input())
gift_price = float(input())

mariah_money = m_quantity * m
mariah_money += z_quantity * z
mariah_money += r_quantity * r
mariah_money += k_quantity * k
mariah_money *= (1 - tax)

diff = mariah_money - gift_price
if diff < 0:
    diff = diff * -1
    print(f'She will have to borrow {math.ceil(diff)} leva.')
else:
    diff = diff
    print(f'She is left with {math.floor(diff)} leva.')