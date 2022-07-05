def factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * factorial(number - 1)


n = int(input())
print(factorial(n))