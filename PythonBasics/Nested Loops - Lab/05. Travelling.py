is_trip_over = False
while True:
    if is_trip_over:
        break
    destination = input()
    if destination == 'End':
        break
    budged = float(input())
    while not is_trip_over:
        saved_money = float(input())
        budged -= saved_money
        if budged <= 0:
            print(f'Going to {destination}!')
            break

