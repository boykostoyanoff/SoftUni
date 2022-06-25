sum_needed = int(input())
cs_sum = 0
cs_peoples = 0
cc_sum = 0
cc_peoples = 0
turn = 1
is_sum_collected = True

while cc_sum + cs_sum < sum_needed:
    data = input()
    if data == 'End':
        is_sum_collected = False
        break
    sum_for_sell = int(data)
    if turn == 1:
        turn = 2
        if sum_for_sell > 100:
            print('Error in transaction!')
        else:
            cs_sum += sum_for_sell
            cs_peoples += 1
            print('Product sold!')
    elif turn == 2:
        turn = 1
        if sum_for_sell < 10:
            print('Error in transaction!')
        else:
            cc_sum += sum_for_sell
            cc_peoples += 1
            print('Product sold!')

if is_sum_collected:
    average_cs = cs_sum / cs_peoples
    print(f'Average CS: {average_cs:.2f}')
    average_cc = cc_sum / cc_peoples
    print(f'Average CC: {average_cc:.2f}')
else:
    print(f'Failed to collect required money for charity.')