import math
data = input()
prime_sum = 0
not_prime_sum = 0


while not data == 'stop':
    number = int(data)
    if number < 0:
        print(f'Number is negative.')
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i) == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += number
        else:
            not_prime_sum += number
    data = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {not_prime_sum}')