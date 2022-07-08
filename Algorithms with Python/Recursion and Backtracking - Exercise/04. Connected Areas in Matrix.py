def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if not matrix[row][col] == '-':
        return 0

    matrix[row][col] = 'v'
    result = 1

    result += explore_area(row - 1, col, matrix)
    result += explore_area(row + 1, col, matrix)
    result += explore_area(row, col - 1, matrix)
    result += explore_area(row, col + 1, matrix)

    return result


rows = int(input())
cols = int(input())

matrix = []
for r in range(rows):
    matrix.append(list(input()))

results = []

for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)
        if not size == 0:
            results.append([row, col, size])

print(f'Total areas found: {len(results)}')
for index, area in enumerate(sorted(results, key=lambda a: a[2], reverse=True)):
    print(f'Area #{index + 1} at ({area[0]}, {area[1]}), size: {area[2]}')