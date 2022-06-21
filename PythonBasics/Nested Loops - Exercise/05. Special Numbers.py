n = int(input())


for number in range(1111, 10000):
    special_n = number
    is_special = True

    while special_n > 0:
        last_digit = special_n % 10
        special_n = special_n // 10
        if last_digit == 0:
            is_special = False
            break
        if not n % last_digit == 0:
            is_special = False
            break
    if is_special:
        print(number, end=' ')

