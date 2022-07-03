control_number = int(input())
counter = 0
password = 'No!'
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == control_number and a < b and c > d:
                    counter += 1
                    number = str(a) + str(b) + str(c) + str(d)
                    print(number, end=' ')
                    if counter == 4:
                        password = f'Password: {number}'
print()
print(password)