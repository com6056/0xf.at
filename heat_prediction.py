import numpy as np

num = 33.

fields_array = [num, num, num, num, num, num, num, num, num, num]
heat_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
heated_array = [0, 0, 0, 161., 0, 0, 0, 0, 0, 0]

field = np.array([fields_array,
                  fields_array,
                  fields_array,
                  fields_array,
                  fields_array,
                  fields_array,
                  fields_array,
                  fields_array,
                  fields_array,
                  fields_array])


heat = np.array([heated_array,
                 heat_array,
                 heat_array,
                 heat_array,
                 heat_array,
                 heat_array,
                 heat_array,
                 heat_array,
                 heat_array,
                 heat_array])


for iteration in range(71):
    for i in range(0, 10):
        # print(i)
        for j in range(0, 10):
            # print(j)
            if i == 0:
                a = 0
            else:
                a = field[i-1, j]
            if i == 9:
                b = 0
            else:
                b = field[i+1, j]
            if j == 0:
                c = 0
            else:
                c = field[i, j-1]
            if j == 9:
                d = 0
            else:
                d = field[i, j+1]
            field[i, j] = (0.25 * (a + b + c + d) + heat[i, j])
    print('Iteration: ' + str(iteration + 1))
    print(field)
print(field[5, 8])
