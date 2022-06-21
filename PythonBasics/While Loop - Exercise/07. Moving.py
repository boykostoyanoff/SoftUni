width = int(input())
length = int(input())
height = int(input())
space = width * length * height

while True:
    boxes = input()
    if boxes == 'Done':
        print(f'{space} Cubic meters left.')
        break

    space -= int(boxes)

    if space <= 0:
        print(f'No more free space! You need {space * -1} Cubic meters more.')
        break
