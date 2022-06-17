import math

n = int(input())

for pow in range(0, n+1 , 2):
    print(int(math.pow(2, pow)))