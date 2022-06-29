number = int(input())

for i1 in range(1, 10):
    for i2 in range(1, 10):
        sum_1_2 = (i1 + i2)
        if number % sum_1_2 == 0:
            for i3 in range(1, 10):
                for i4 in range(1, 10):
                    sum_3_4 = i3 + i4
                    if sum_1_2 == sum_3_4:
                        print(i1*1000 + i2*100 + i3*10 + i4, end=' ')