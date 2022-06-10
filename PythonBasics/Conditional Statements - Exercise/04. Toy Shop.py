puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

money_from_toys = puzzle_price * puzzle_count
money_from_toys += doll_price * doll_count
money_from_toys += bear_price * bear_count
money_from_toys += minion_price * minion_count
money_from_toys += truck_price * truck_count

toys_count = puzzle_count + doll_count + bear_count + minion_count + truck_count

if toys_count >= 50:
    money_from_toys = money_from_toys - (money_from_toys * 0.25)
rent_price = money_from_toys * 0.10
saved_money = money_from_toys - rent_price

if saved_money >= trip_price:
    print(f'Yes! {(saved_money - trip_price):.2f} lv left.')
else:
    print(f'Not enough money! {(trip_price - saved_money):.2f} lv needed.')