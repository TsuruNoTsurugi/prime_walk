# prime_walk.py (to generate prime_walk.png) is licensed under a MIT License.
# Author: TsuruNoTsurugi
# Date: 2023-12-03

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

data = "prime_num.txt"  # prime_num.txt is a text file containing prime numbers
"""You have to generate prime_num.txt by yourself."""

path = "prime_walk.png" # prime_walk.png is a png file containing prime walk

"""Example: prime_num.txt is splited by comma."""
f = open(data, "r")
prime_data = f.read().split(",")
prime_data = np.int_(prime_data)

# prime walk
x = [0];y = [0];z = [0]
for i in range(len(prime_data)-1):
    difference = prime_data[i+1] - prime_data[i]
    if (i+1) % 4 == 1:#x+
        for j in range(difference):
            x.append(x[-1]+1)
            y.append(y[-1])
            z.append(z[-1]+1)
    if (i+1) % 4 == 2:#y+
        for j in range(difference):
            x.append(x[-1])
            y.append(y[-1]+1)
            z.append(z[-1]+1)
    if (i+1) % 4 == 3:#x-
        for j in range(difference):
            x.append(x[-1]-1)
            y.append(y[-1])
            z.append(z[-1]+1)
    if (i+1) % 4 == 0:#y-
        for j in range(difference):
            x.append(x[-1])
            y.append(y[-1]-1)
            z.append(z[-1]+1)
            
# plot
fig = plt.figure(figsize=(16.5354,11.6929))
ax1 = fig.add_subplot(111)
ax1.tick_params(labelbottom=False,
               labelleft=False,
               labelright=False,
               labeltop=False)
ax1.tick_params(bottom=False,
               left=False,
               right=False,
               top=False)
ppi=72 # pixels per inch
xmin,xmax = min(x), max(x)
ymin,ymax = min(y), max(y)
size=0.25
ax_length=ax1.bbox.get_points()[1][0]-ax1.bbox.get_points()[0][0]
ax_point = ax_length*ppi/fig.dpi
xsize=xmax-xmin
fact=ax_point/xsize
size*=2*fact
plt.scatter(x, y,
            s=size**2, # size of marker
            c=z,       # color of marker
            cmap='viridis', # color map (You can change it. See https://matplotlib.org/stable/tutorials/colors/colormaps.html)
            marker='s', # shape of marker
            norm=Normalize(vmin=0, vmax=max(z)))
plt.tight_layout()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.savefig(path, format="png", dpi=2000) # save as png file