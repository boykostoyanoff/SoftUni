steps_for_day = 0

while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        steps_for_day += steps
        break
    steps = int(steps)
    steps_for_day += steps
    if steps_for_day >= 10000:
        break

steps_for_day -= 10000
if steps_for_day < 0:
    print(f'{steps_for_day * -1} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{steps_for_day} steps over the goal!')