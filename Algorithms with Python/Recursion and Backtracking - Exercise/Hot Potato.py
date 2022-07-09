def hot_potato(kids, turn, index):
    if len(kids) == 1:
        print(f'Last is {kids.pop()}')
        return
    index = (index + n - 1) % len(kids)
    print(f'Removed {kids.pop(index)}')
    hot_potato(kids, n, index)


kids = list(input().split(' '))
n = int(input())
hot_potato(kids, n, 0)