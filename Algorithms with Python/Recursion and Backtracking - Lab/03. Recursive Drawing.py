def recursive_print(number):
    if number == 0:
        return
    print(number * '*')
    recursive_print(number - 1)
    print('#' * number)


n = int(input())
recursive_print(n)