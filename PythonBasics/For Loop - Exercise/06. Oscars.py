actor_name = input()
academy_points = float(input())
evaluators = int(input())

nominate_points = 1250.5
actor_points = academy_points

for _ in range(evaluators):
    name = input()
    points = float(input())
    actor_points += len(name) * points / 2
    if actor_points > nominate_points:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!')
        break

if actor_points <= nominate_points:
    points_needed = nominate_points - actor_points
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')