result = 'error'
town = input()
sales = float(input())

commission = 0

if town == 'Sofia':
    if sales < 0:
        pass
    elif 0 <= sales <= 500:
        commission = 5
    elif sales <= 1000:
        commission = 7
    elif sales <= 10000:
        commission = 8
    elif sales > 10000:
        commission = 12
elif town == 'Varna':
    if sales < 0:
        pass
    elif 0 <= sales <= 500:
        commission = 4.5
    elif sales <= 1000:
        commission = 7.5
    elif sales <= 10000:
        commission = 10
    elif sales > 10000:
        commission = 13
elif town == 'Plovdiv':
    if sales < 0:
        pass
    elif 0 <= sales <= 500:
        commission = 5.5
    elif sales <= 1000:
        commission = 8
    elif sales <= 10000:
        commission = 12
    elif sales > 10000:
        commission = 14.5

if commission > 0:
    result = sales * commission / 100
    print(f'{result:.2f}')
else:
    print(result)