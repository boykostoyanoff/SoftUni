protective_nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

protective_nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

total_price = 0
total_price += (protective_nylon + 2) * protective_nylon_price
total_price += paint_price * (paint * 1.1)
total_price += paint_thinner * paint_thinner_price
total_price += 0.40
total_price += total_price * 0.30 * hours

print(total_price)
