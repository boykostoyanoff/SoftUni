groups_count = int(input())
k1 = 0
k2 = 0
k3 = 0
k4 = 0
k5 = 0

for _ in range(groups_count):
    group_size = int(input())
    if group_size <= 5:
        k1 += group_size
    elif group_size <= 12:
        k2 += group_size
    elif group_size <= 25:
        k3 += group_size
    elif group_size <= 40:
        k4 += group_size
    elif group_size > 40:
        k5 += group_size

all_people = k1 + k2 + k3 + k4 + k5
print(f'{(k1 / all_people * 100):.2f}%')
print(f'{(k2 / all_people * 100):.2f}%')
print(f'{(k3 / all_people * 100):.2f}%')
print(f'{(k4 / all_people * 100):.2f}%')
print(f'{(k5 / all_people * 100):.2f}%')


