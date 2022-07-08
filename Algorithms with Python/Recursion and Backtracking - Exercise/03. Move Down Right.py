def find_ways(board, ways, r, c):
    if r >= rows or c >= cols:
        return
    if board[r][c] == 'end':
        ways.append(1)
        return
    else:
        find_ways(board, ways, r + 1, c)
        find_ways(board, ways, r, c + 1)


rows = int(input())
cols = int(input())
ways = []

board = [['-'] * cols for _ in range(rows)]
board[rows - 1][cols - 1] = 'end'

find_ways(board, ways, 0, 0)
print(len(ways))