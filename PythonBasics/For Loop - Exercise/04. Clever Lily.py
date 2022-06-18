lilly_brother_takes = 1
lilly_money_gift = 0
saved_money = 0

lilly_age = int(input())
wash_machine_price = float(input())
toy_price = int(input())

for year in range(1, lilly_age + 1):
    if year % 2 == 0:
        lilly_money_gift += 10
        saved_money += lilly_money_gift - lilly_brother_takes
    else:
        saved_money += toy_price

if wash_machine_price <= saved_money:
    print(f'Yes! {(saved_money - wash_machine_price):.2f}')
else:
    print(f'No! {(wash_machine_price - saved_money):.2f}')
