x = float(input())
y = float(input())
h = float(input())

door_area = 1.2 * 2
window_area = 1.5 * 1.5

front_wall_area = x * x
side_wall_area = x * y
all_walls_area = 2 * (front_wall_area + side_wall_area)
area_for_paint = all_walls_area - door_area - window_area * 2
green_paint_needed = area_for_paint / 3.4

front_roof_area = x * h / 2
side_roof_area = x * y
all_roof_area = 2 * (front_roof_area + side_roof_area)
red_paint_needed = all_roof_area / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')