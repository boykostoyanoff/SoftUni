import math

peoples = int(input())
tax = float(input())
sun_lounger = float(input())
umbrella = float(input())

total_tax = peoples * tax
total_sun_lounger = math.ceil(peoples * 0.75) * sun_lounger
total_umbrella = math.ceil(peoples / 2) * umbrella

total_sum = total_tax + total_sun_lounger + total_umbrella

print(f'{total_sum:.2f} lv.')