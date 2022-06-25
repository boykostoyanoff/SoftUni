ch = input()
is_c = False
is_o = False
is_n = False
result = ''

while not ch == 'End':

    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        if ch == 'c' and not is_c:
            is_c = True
        elif ch == 'o' and not is_o:
            is_o = True
        elif ch == 'n' and not is_n:
            is_n = True
        else:
            result += ch

    if is_n and is_o and is_c:
        print(result, end=' ')
        result = ''
        is_n = is_c = is_o = False

    ch = input()
