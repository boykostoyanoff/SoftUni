interest_wanted = float(input())
total_price = 0

while True:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        print(f'We need {(interest_wanted - total_price):.2f} leva more.')
        break

    cocktail_quantity = int(input())
    cocktail_price = len(cocktail_name)
    order_price = cocktail_price * cocktail_quantity
    if not order_price == 0 and order_price % 2 == 1:
        order_price *= 0.75

    total_price += order_price

    if total_price >= interest_wanted:
        print('Target acquired.')
        break

print(f'Club income - {total_price:.2f} leva.')