# prime_ulam.py (to generate prime_ulam.png) is licensed under a MIT License.
# Author: TsuruNoTsurugi
# Date: 2023-12-03

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np
from sympy import sieve

data = "prime_num.txt"  # prime_num.txt is a text file containing prime numbers
"""You have to generate prime_num.txt by yourself."""

path = "prime_ulam.png" # prime_ulam.png is a png file containing prime ulam spiral

"""Example: prime_num.txt is splited by comma."""
f = open(data, "r")
prime_data = f.read().split(",")
prime_data = np.int_(prime_data)
max_data = max(prime_data)

# prime ulam spiral
x = [0];y = [0]
n = 1
for i in range(550):
    for j in range(n):
        x.append(x[-1] + 1)
        y.append(y[-1])
    for j in range(n):
        x.append(x[-1])
        y.append(y[-1] + 1)
    for j in range(n + 1):
        x.append(x[-1] - 1)
        y.append(y[-1])
    for j in range(n + 1):
        x.append(x[-1])
        y.append(y[-1] - 1)
    n += 2
prime_x = []
prime_y = []
for i in range(len(x)):
    if i in prime_data:
        prime_x.append(x[i-1])
        prime_y.append(y[i-1])
fig = plt.figure(figsize=(11.6929,16.5354))
ax1 = fig.add_subplot(111)
ax1.tick_params(labelbottom=False,
               labelleft=False,
               labelright=False,
               labeltop=False)
ax1.tick_params(bottom=False,
               left=False,
               right=False,
               top=False)
ppi=72
xmin,xmax = min(x), max(x)
ymin,ymax = min(y), max(y)
size=0.25
ax_length=ax1.bbox.get_points()[1][0]-ax1.bbox.get_points()[0][0]
ax_point = ax_length*ppi/fig.dpi
xsize=xmax-xmin
fact=ax_point/xsize
size*=2*fact
plt.scatter(prime_x, prime_y,
            s=size**2, c="black", # You can change the color of the points.(see https://matplotlib.org/stable/tutorials/colors/colormaps.html)
            marker='s')
plt.tight_layout()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.savefig(path, format="png", dpi=2000) # save as png file