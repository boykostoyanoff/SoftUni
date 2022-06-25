while True:
    number = float(input())
    if number < 0:
        print('Negative number!')
        break
    print(f'Result: {(number * 2):.2f}')