bottles_count = int(input())

bottles_volume = 750 * bottles_count
plate_cost = 5
pot_cost = 15
turn = 0
clear_plates = 0
clear_pots = 0

while True:
    dishes = input()
    if dishes == 'End':
        print('Detergent was enough!')
        print(f'{clear_plates} dishes and {clear_pots} pots were washed.')
        print(f'Leftover detergent {bottles_volume} ml.')
        break

    dishes = int(dishes)
    turn += 1

    if turn < 3:
        clear_plates += dishes
        bottles_volume -= dishes * plate_cost
    else:
        turn = 0
        clear_pots += dishes
        bottles_volume -= dishes * pot_cost

    if bottles_volume < 0:
        print(f'Not enough detergent, {abs(bottles_volume)} ml. more necessary!')
        break
