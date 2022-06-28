start = ord(input())
end = ord(input())
missed = ord(input())
counter = 0

for ch1 in range(start, end + 1):
    if not ch1 == missed:
        for ch2 in range(start, end + 1):
            if not ch2 == missed:
                for ch3 in range(start, end + 1):
                    if not ch3 == missed:
                        print(chr(ch1) + chr(ch2) + chr(ch3), end=' ')
                        counter += 1
print(counter)
