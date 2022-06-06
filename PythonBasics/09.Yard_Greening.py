price_per_meter = 7.61
discount = 0.18

area = float(input())

price = price_per_meter * area
discount_price = price * discount
total_price = price - discount_price

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount_price} lv.")
