type_of_projection = input()
row = int(input())
col = int(input())
premiere_price = 12.00
normal_price = 7.50
discount_price = 5.00
result = row * col

if type_of_projection == 'Premiere':
    result *= premiere_price
elif type_of_projection == 'Normal':
    result *= normal_price
else:
    result *= discount_price

print(f'{result:.2f} leva')