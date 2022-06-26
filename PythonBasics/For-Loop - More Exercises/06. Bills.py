months = int(input())
electricity = 0
water = 20 * months
internet = 15 * months
other = 0

for _ in range(months):
    electricity_for_this_month = float(input())
    electricity += electricity_for_this_month

other += (electricity + water + internet) * 1.2
result = (other + electricity + water + internet) / months
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {result:.2f} lv")