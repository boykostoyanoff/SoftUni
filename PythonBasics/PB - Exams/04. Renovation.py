import math

height = float(input())
width = float(input())
part_not_painted = int(input())
part_for_paint = math.ceil(width * height * (1 - part_not_painted / 100) * 4)
paint_needed = part_for_paint

while True:
    data = input()
    if data == 'Tired!':
        print(f'{paint_needed} quadratic m left.')
        break
    paint = int(data)

    paint_needed -= paint

    if paint_needed < 0:
        print(f'All walls are painted and you have {abs(paint_needed)} l paint left!')
        break

    if paint_needed == 0:
        print('All walls are painted! Great job, Pesho!')
        break