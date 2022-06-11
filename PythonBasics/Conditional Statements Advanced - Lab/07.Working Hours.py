hour = int(input())
day_of_week = input()
if 10 <= hour <= 18 and not day_of_week == 'Sunday':
    print('open')
else:
    print('closed')