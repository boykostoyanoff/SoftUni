tax_for_year = int(input())
shoes_price = tax_for_year * 0.60
clothes_price = shoes_price * 0.80
ball_price = clothes_price * 0.25
accessories_price = ball_price * 0.20

total_price = tax_for_year + shoes_price + clothes_price + ball_price + accessories_price

print(total_price)