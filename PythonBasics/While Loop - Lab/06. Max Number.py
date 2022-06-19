data = input()
max_number = ''

while not data == 'Stop':
    if max_number == '':
        max_number = int(data)
        continue
    if max_number < int(data):
        max_number = int(data)
    data = input()
print(max_number)