first_couple_start = int(input())
second_couple_start = int(input())
first_couple_end = first_couple_start + int(input())
second_couple_end = second_couple_start + int(input())


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for f in range(first_couple_start, first_couple_end + 1):
    for s in range(second_couple_start, second_couple_end + 1):
        if is_prime(f) and is_prime(s):
            print(str(f) + str(s))
