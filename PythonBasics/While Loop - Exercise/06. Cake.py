cake_weight = int(input())
cake_height = int(input())

cake_pieces = cake_height * cake_weight

while True:
    pieces_taken = input()
    if pieces_taken == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break

    cake_pieces -= int(pieces_taken)

    if cake_pieces < 0:
        print(f'No more cake left! You need {cake_pieces * -1} pieces more.')
        break
