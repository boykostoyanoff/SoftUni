def find_all_paths(row, col, lab, direction, path):
    if row < 0 or row >= len(lab) or col < 0 or col >= len(lab[0]):
        return
    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
    else:
        lab[row][col] = 'v'
        find_all_paths(row + 1, col, lab, 'D', path)
        find_all_paths(row - 1, col, lab, 'U', path)
        find_all_paths(row, col + 1, lab, 'R', path)
        find_all_paths(row, col - 1, lab, 'L', path)
        lab[row][col] = '-'

    path.pop()


labyrinth_rows = int(input())
labyrinth_cols = int(input())

labyrinth = [[p for p in input()] for _ in range(labyrinth_rows)]

find_all_paths(0, 0, labyrinth, '', [])
