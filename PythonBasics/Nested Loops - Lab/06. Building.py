stages = int(input())
rooms = int(input())
letter = 'L'

for s in range(stages, 0, -1):
    result = ''
    for r in range(rooms):
        result += f'{letter}{s}{r} '

    print(result.strip())
    if (s + 1) % 2 == 0:
        letter = 'O'
    else:
        letter = 'A'
