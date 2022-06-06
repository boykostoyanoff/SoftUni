sum_of_deposit = float(input())
time_of_deposit = int(input())
year_interest_rate = float(input()) / 100

total_sum = sum_of_deposit + time_of_deposit * ((sum_of_deposit * year_interest_rate) / 12)

print(total_sum)