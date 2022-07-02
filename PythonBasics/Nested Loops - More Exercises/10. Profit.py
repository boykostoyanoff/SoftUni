one_lev = int(input())
two_lev = int(input())
five_lev = int(input())
total_sum = int(input())

for one in range(0, one_lev + 1):
    for two in range(0, two_lev + 1):
        for five in range(0, five_lev + 1):
            if one * 1 + two * 2 + five * 5 == total_sum:
                print(f'{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {total_sum} lv.')