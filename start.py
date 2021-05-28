import matplotlib.pyplot as plt
import numpy as np
from random import randint


def rand_dX(a, b, c):
    n_sum = 0
    for n1 in range(c):
        n_sum += randint(a,b)
    return n_sum

points_Nr = 1000000
dice_Value_max = 6
dices_Nr = 3

xs = []
ys = []
for n1 in range(1 * dices_Nr, dice_Value_max * dices_Nr + 1):
    xs.append(n1)
    ys.append(0)
print(xs)
print(ys)

for n2 in range(1, points_Nr):
    dices_sum = rand_dX(1, dice_Value_max, dices_Nr)
    index = dices_sum - 1 * dices_Nr
    # print(n2, dices_sum, index)
    ys[index] += dices_sum

   
print(ys)

plt.plot(xs, ys)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()