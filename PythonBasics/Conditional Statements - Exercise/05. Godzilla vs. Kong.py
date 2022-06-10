budged = float(input())
statists = int(input())
dress_price_for_one_statist = float(input())

decor_price = budged * 0.10
price_for_dresses = statists * dress_price_for_one_statist

if statists > 150:
    price_for_dresses *= 0.90

total_cost = decor_price + price_for_dresses

if budged - total_cost < 0:
    print(f'Not enough money!')
    print(f"Wingard needs {(total_cost - budged):.2f} leva more.")
else:
    print(f'Action!')
    print(f'Wingard starts filming with {(budged - total_cost):.2f} leva left.')