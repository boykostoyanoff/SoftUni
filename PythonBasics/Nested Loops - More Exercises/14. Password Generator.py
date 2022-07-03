n = int(input())
l = int(input())

for s1 in range(1, n + 1):
    for s2 in range(1, n + 1):
        for s3 in range(ord('a'), ord('a') + l):
            for s4 in range(ord('a'), ord('a') + l):
                for s5 in range(1, n + 1):
                    if s5 > s1 and s5 > s2:
                        print(str(s1) + str(s2) + chr(s3) + chr(s4) + str(s5), end=' ')