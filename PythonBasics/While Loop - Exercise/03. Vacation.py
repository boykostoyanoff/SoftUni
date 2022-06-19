trip_price = float(input())
saved_money = float(input())
days_spend_money = 0
days = 0

while True:
    action = input()
    money = float(input())
    days += 1
    if action == 'save':
        days_spend_money = 0
        saved_money += money
        if saved_money >= trip_price:
            print(f'You saved the money for {days} days.')
            break
    elif action == 'spend':
        days_spend_money += 1
        if days_spend_money == 5:
            print(f"You can't save the money.")
            print(days)
            break
        saved_money -= money
        if saved_money < 0:
            saved_money = 0