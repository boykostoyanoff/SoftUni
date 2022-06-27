n = int(input())

upper_down_line = '*' * (2 * n) + ' ' * n + '*' * (2 * n)
print(upper_down_line)

middle_line = '*' + '/' * (2 * n - 2) + '*' + ' ' * n + '*' + '/' * (2 * n - 2) + '*'
middle_line_with_line = '*' + '/' * (2 * n - 2) + '*' + '|' * n + '*' + '/' * (2 * n - 2) + '*'
for row in range(n - 2):
    if row == (n-1) // 2 - 1:
        print(middle_line_with_line)
    else:
        print(middle_line)

print(upper_down_line)