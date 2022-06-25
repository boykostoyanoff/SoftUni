x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if x1 < x < x2 and y1 < y < y2:
    print('Inside / Outside')
elif x1 > x or x2 < x or y1 > y or y2 < y:
    print('Inside / Outside')
else:
    print('Border')