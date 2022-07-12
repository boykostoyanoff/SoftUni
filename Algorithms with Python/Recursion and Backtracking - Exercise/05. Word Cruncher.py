def find_combinations(parts, target_word, my_word, index, banned_index, my_word_len):
    if index > len(parts) or my_word_len > len(target_word):
        return

    if my_word_len == len(target_word):
        if ''.join(my_word) == target_word:
            print(' '.join(my_word))

    for idx in range(len(parts)):
        if idx in banned_index:
            continue

        my_word.append(parts[idx])
        banned_index.append(idx)
        my_word_len += len(parts[idx])

        find_combinations(parts, target_word, my_word, index + 1, banned_index, my_word_len)

        my_word.pop()
        banned_index.pop()
        my_word_len -= len(parts[idx])


parts = list(input().split(', '))
target_word = input()
my_word = []

find_combinations(parts, target_word, my_word, 0, [], 0)
