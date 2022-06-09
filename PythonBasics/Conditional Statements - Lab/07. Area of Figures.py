from math import pi
figure_type = input()
figure_area = 0
a = float(input())
if figure_type == 'square':
    figure_area = a * a
elif figure_type == 'rectangle':
    b = float(input())
    figure_area = a * b
elif figure_type == 'circle':
    figure_area = a * a * pi
else:
    b = float(input())
    figure_area = a * b / 2

print(f'{figure_area:.3f}')