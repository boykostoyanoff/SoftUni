mackerel_price = float(input())
sprat_price = float(input())
bonito_quantity = float(input())
horse_mackerel_quantity = float(input())
mussels_quantity = int(input())

mussels_price = 7.50
bonito_price = mackerel_price * 1.60
horse_mackerel_price = sprat_price * 1.80

total_price = 0
total_price += bonito_quantity * bonito_price + horse_mackerel_quantity * horse_mackerel_price + mussels_quantity * mussels_price

print(f'{total_price:.2f}')