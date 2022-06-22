h = float(input()) * 100
w = float(input()) * 100

area = w * h
w_without_middle = w - 100
w_desks = w_without_middle // 70

h_desks = h // 120

desks = h_desks * w_desks - 3
print(int(desks))