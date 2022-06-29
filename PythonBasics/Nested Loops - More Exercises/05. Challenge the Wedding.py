man_count = int(input())
woman_count = int(input())
table_max = int(input())
date_counter = 0

for m in range(1, man_count + 1):
    if date_counter == table_max:
        break
    for w in range(1, woman_count + 1):
        if date_counter == table_max:
            break
        print(f'({m} <-> {w})', end=' ')
        date_counter += 1