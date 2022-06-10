import math

film_name = input()
film_length = int(input())
lunch_break = int(input())

time_for_lunch = lunch_break * (1 / 8)
time_for_rest = lunch_break * (1 / 4)
time = lunch_break - film_length - time_for_rest - time_for_lunch


if time >= 0:
    time = math.ceil(time)
    print(f'You have enough time to watch {film_name} and left with {time} minutes free time.')
else:
    time *= -1
    time = math.ceil(time)
    print(f"You don't have enough time to watch {film_name}, you need {time} more minutes.")