data = input()
min_number = ''

while not data == 'Stop':
    if min_number == '':
        min_number = int(data)
        continue
    if min_number > int(data):
        min_number = int(data)
    data = input()
print(min_number)