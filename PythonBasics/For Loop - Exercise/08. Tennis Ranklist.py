tournament_count = int(input())
starting_points = int(input())

w_points = 2000
f_points = 1200
sf_points = 720
wins = 0
points = starting_points

for _ in range(tournament_count):
    stage = input()
    if stage == 'W':
        wins += 1
        points += w_points
    elif stage == 'F':
        points += f_points
    elif stage == 'SF':
        points += sf_points

print(f'Final points: {points}')
average_points = (points - starting_points) // tournament_count
print(f'Average points: {average_points}')
print(f'{(wins / tournament_count * 100):.2f}%')