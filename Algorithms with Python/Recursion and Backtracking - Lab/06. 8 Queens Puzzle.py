def n_queen(n):
    cols = set()
    positive_diagonals = set()
    negative_diagonals = set()

    board = []
    [board.append(['-'] * 8) for _ in range(q)]

    def backtracking(row):
        if row == n:
            [print(' '.join(r)) for r in board]
            print()

        for col in range(n):
            if col in cols or row + col in positive_diagonals or row - col in negative_diagonals:
                continue
            else:
                board[row][col] = '*'
                cols.add(col)
                negative_diagonals.add(row - col)
                positive_diagonals.add(row + col)
                backtracking(row + 1)

                board[row][col] = '-'
                cols.remove(col)
                negative_diagonals.remove(row - col)
                positive_diagonals.remove(row + col)

    backtracking(0)
    return


q = 8

n_queen(q)
