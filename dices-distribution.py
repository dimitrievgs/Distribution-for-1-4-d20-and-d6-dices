import matplotlib.pyplot as plt
import numpy as np
from random import randint

# https://matplotlib.org/3.1.0/gallery/pyplots/pyplot_scales.html#sphx-glr-gallery-pyplots-pyplot-scales-py

def rand_dX(a, b, c):
    n_sum = 0
    for n1 in range(c):
        n_sum += randint(a,b)
    return n_sum

points_Nr = 500000
dice_Value_max = 20
dices_Nr_max = 4

xss = []
yss = []
ys_maxs = []
titles = []

for dNr in range(1, dices_Nr_max + 1):
    dices_Nr = dNr
    print(dNr)

    xs = []
    ys = []
    for n1 in range(1 * dices_Nr, dice_Value_max * dices_Nr + 1):
        xs.append(n1)
        ys.append(0)

    for n2 in range(1, points_Nr):
        dices_sum = rand_dX(1, dice_Value_max, dices_Nr)
        index = dices_sum - 1 * dices_Nr
        ys[index] += 1

    ys_max = max(ys)
    title = str(dices_Nr) + 'd' + str(dice_Value_max)
    
    if (dNr == 1):
        title += ", # of throws = " + str(points_Nr)

    xss.append(xs)
    yss.append(ys)
    ys_maxs.append(ys_max)
    titles.append(title)

####

plot_color = 'gray' # 'skyblue'
marker_color = 'red' # 'blue'

def make_plot(axs):
    box = dict(facecolor='yellow', pad=5, alpha=0.2)

    ax1 = axs[0, 0]
    ax1.plot(xss[0],yss[0], marker='o', markerfacecolor=marker_color, markersize=5, color=plot_color, linewidth=1)
    ax1.set_title(titles[0])
    ax1.set_ylim(0, ys_maxs[0] * 1.1)

    
    ax3 = axs[1, 0]
    ax3.plot(xss[1],yss[1], marker='o', markerfacecolor=marker_color, markersize=5, color=plot_color, linewidth=1)
    ax3.set_title(titles[1])
    ax3.set_ylim(0, ys_maxs[1] * 1.1)

    ax2 = axs[0, 1]
    ax2.plot(xss[2],yss[2], marker='o', markerfacecolor=marker_color, markersize=5, color=plot_color, linewidth=1)
    ax2.set_title(titles[2])
    ax2.set_ylim(0, ys_maxs[2] * 1.1)

    ax4 = axs[1, 1]
    ax4.plot(xss[3],yss[3], marker='o', markerfacecolor=marker_color, markersize=5, color=plot_color, linewidth=1)
    ax4.set_title(titles[3])
    ax4.set_ylim(0, ys_maxs[3] * 1.1)
    


# Plot 1:
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.3,
                    wspace=0.35)
make_plot(axs)

# just align the last column of axes:
fig.align_ylabels(axs[:, 1])
fig.savefig('d' + str(dice_Value_max) + ".png", dpi = 300)
plt.show()
