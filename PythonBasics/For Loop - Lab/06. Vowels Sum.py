text = input()
vowels_sum = 0
for ch in text:
    if ch == 'a':
        vowels_sum += 1
    elif ch == 'e':
        vowels_sum += 2
    elif ch == 'i':
        vowels_sum += 3
    elif ch == 'o':
        vowels_sum += 4
    elif ch == 'u':
        vowels_sum += 5
print(vowels_sum)