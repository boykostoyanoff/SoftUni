first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    c_number = number
    odd_sum = 0
    even_sum = 0
    for i in range(1, 7):
        if i % 2 == 1:
            odd_sum += c_number % 10
        else:
            even_sum += c_number % 10
        c_number = c_number // 10

    if odd_sum == even_sum:
        print(number, end=' ')