town_name = input()
package_type = input()
is_vip = input()
if is_vip == 'no':
    is_vip = False
else:
    is_vip = True

days = int(input())
price_per_day = 0
discount = 0

possible_towns = ['Bansko', 'Borovets', 'Varna', 'Burgas']
possible_packages = ["noEquipment",  "withEquipment", "noBreakfast", "withBreakfast"]

if days < 1:
    print("Days must be positive number!")
elif town_name not in possible_towns or package_type not in possible_packages:
    print("Invalid input!")
else:
    if package_type == 'withEquipment':
        price_per_day = 100
        if is_vip:
            discount = 10
    elif package_type == 'noEquipment':
        price_per_day = 80
        if is_vip:
            discount = 5
    elif package_type == 'withBreakfast':
        price_per_day = 130
        if is_vip:
            discount = 12
    elif package_type == 'noBreakfast':
        price_per_day = 100
        if is_vip:
            discount = 7

    if days > 7:
        days -= 1

    total_price = days * price_per_day * (1 - discount / 100)
    print(f'The price is {total_price:.2f}lv! Have a nice time!')