turns_count = int(input())
result = 0
interval_0_9 = 0
interval_10_19 = 0
interval_20_29 = 0
interval_30_39 = 0
interval_40_50 = 0
invalid_numbers = 0

for _ in range(turns_count):
    number = int(input())
    if number < 0 or number > 50:
        invalid_numbers += 1
        result /= 2

    elif 0 <= number <= 9:
        result += number * 0.20
        interval_0_9 += 1

    elif 10 <= number <= 19:
        result += number * 0.30
        interval_10_19 += 1

    elif 20 <= number <= 29:
        result += number * 0.40
        interval_20_29 += 1

    elif 30 <= number <= 39:
        result += 50
        interval_30_39 += 1

    elif 40 <= number <= 50:
        result += 100
        interval_40_50 += 1


print(f"{result:.2f}")
result = interval_0_9 / turns_count * 100
print(f"From 0 to 9: {result:.2f}%")
result = interval_10_19 / turns_count * 100
print(f"From 10 to 19: {result:.2f}%")
result = interval_20_29 / turns_count * 100
print(f"From 20 to 29: {result:.2f}%")
result = interval_30_39 / turns_count * 100
print(f"From 30 to 39: {result:.2f}%")
result = interval_40_50 / turns_count * 100
print(f"From 40 to 50: {result:.2f}%")
result = invalid_numbers / turns_count * 100
print(f"Invalid numbers: {result:.2f}%")