h_p_l_price = 2.00
h_e_z_price = 3.75
r_p_l_price = 4.10
r_e_z_price = 4.50
l_p_l_price = 2.50
l_e_z_price = 4.15

tax_holiday = 1.15
bouquet_arranging = 2.00

h_quantity = int(input())
r_quantity = int(input())
l_quantity = int(input())
season = input()
is_holiday = input()
total = 0
tax = 1

if is_holiday == 'Y':
    tax = tax_holiday

if season in ['Spring', 'Summer']:
    h_price = h_p_l_price * h_quantity * tax
    r_price = r_p_l_price * r_quantity * tax
    l_price = l_p_l_price * l_quantity * tax
    total = h_price + l_price + r_price
    if l_quantity > 7 and season == 'Spring':
        total *= 0.95
else:
    h_price = h_e_z_price * h_quantity * tax
    r_price = r_e_z_price * r_quantity * tax
    l_price = l_e_z_price * l_quantity * tax
    total = h_price + l_price + r_price
    if r_quantity >= 10 and season == 'Winter':
        total *= 0.90

if h_quantity + r_quantity + l_quantity > 20:
    total = total * 0.80

total += bouquet_arranging

print(f'{total:.2f}')