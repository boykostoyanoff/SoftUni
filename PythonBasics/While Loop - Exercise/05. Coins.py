money = float(input())
money = int(money * 100)
coins = 0
nomination = 200

while money > 0:

    if money % nomination >= 0:
        c = money // nomination
        money -= nomination * c

    coins += c

    if nomination == 200:
        nomination = 100
    elif nomination == 100:
        nomination = 50
    elif nomination == 50:
        nomination = 20
    elif nomination == 20:
        nomination = 10
    elif nomination == 10:
        nomination = 5
    elif nomination == 5:
        nomination = 2
    elif nomination == 2:
        nomination = 1
    elif nomination == 1:
        break


print(coins)