pencil_price = 5.80
marker_price = 7.20
detergent_price = 1.20

pencil_count = int(input())
marker_count = int(input())
detergent_count = int(input())
reduction = int(input())

total_sum = pencil_count * pencil_price
total_sum += marker_count * marker_price
total_sum += detergent_count * detergent_price
total_sum -= total_sum * reduction / 100

print(total_sum)
