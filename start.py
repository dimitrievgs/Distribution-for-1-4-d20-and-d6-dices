import matplotlib.pyplot as plt
import numpy as np
from random import randint


def rand_dX(a, b, c):
    n_sum = 0
    for n1 in range(c):
        n_sum += randint(a,b)
    return n_sum

points_Nr = 1000000
dice_Value_max = 20
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
    ys[index] += 1

ys_max = max(ys)
print(ys)

_label = "Distribution of " + str(dices_Nr) + 'd' + str(dice_Value_max) + ", # of throws = " + str(points_Nr)

fig, ax = plt.subplots()
ax.plot(xs, ys)

ax.set(xlabel='sum of dices', ylabel='freq of occurence',
       title=_label)
ax.grid()
plt.ylim(0, ys_max * 1.1)

fig.savefig("test.png")
plt.show()