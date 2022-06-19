total_balance = 0
contribution = input()
while not contribution == 'NoMoreMoney':
    contribution = float(contribution)
    if contribution < 0:
        print(f'Invalid operation!')
        break
    else:
        print(f'Increase: {contribution:.2f}')
        total_balance += contribution

    contribution = input()

print(f'Total: {total_balance:.2f}')