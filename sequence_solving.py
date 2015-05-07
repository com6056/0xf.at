sequences = open('sequences.txt')
a = sequences.readline().strip().split(',')
b = sequences.readline().strip().split(',')
c = sequences.readline().strip().split(',')
d = sequences.readline().strip().split(',')
sequence_list = [a, b, c, d]


def equation(x, k1, k2):
    return pow(x + 2, k1) % ((k1 - 2) * (k2 - 2))

answer = 0

for sequence in sequence_list:
    k1_val = 1000
    k2_val = 1000
    num = 0
    while True:
        num = equation(1, k1_val, k2_val)
        if num == int(sequence[0]):
            answer += equation(4, k1_val, k2_val)
            break
        if k1_val < 1200 and k2_val < 1201:
            k1_val += 1
        elif k1_val == 1200 and k2_val < 1200:
            k1_val = 1000
            k2_val += 1
        else:
            break

print(answer)
