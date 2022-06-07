chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery_price = 2.50

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegan_menu_count = int(input())

total_sum = 0
total_sum += chicken_menu_count * chicken_menu_price
total_sum += fish_menu_count * fish_menu_price
total_sum += vegan_menu_count * vegan_menu_price

dessert_price = total_sum * 0.20
total_sum += dessert_price
total_sum += delivery_price

print(total_sum)
