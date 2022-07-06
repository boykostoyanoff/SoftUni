def gen_vectors(vector, index):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        gen_vectors(vector, index + 1)


n = int(input())
vector = [0] * n

gen_vectors(vector, 0)
