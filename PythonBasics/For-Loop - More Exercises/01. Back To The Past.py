money_have = float(input())
year_to_live = int(input())
ivan_age = 18

for year in range(1800, year_to_live + 1):
    money_have -= 12000
    if not year % 2 == 0:
        money_have -= 50 * ivan_age
    ivan_age += 1


if money_have >= 0:
    print(f'Yes! He will live a carefree life and will have {money_have:.2f} dollars left.')
else:
    print(f'He will need {abs(money_have):.2f} dollars to survive.')