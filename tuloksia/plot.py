#!/usr/bin/env python3

import matplotlib.pyplot as plt
import csv
import sys
import os
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

x0 = []
y0 = []
y1 = []

num_args = len(sys.argv)

with open(sys.argv[1],'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(len(row) > 1):
            x0.append(int(row[0]))
            y0.append(int(row[1]))

with open(sys.argv[2],'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(len(row) > 1):
            y1.append(int(row[1]))


plt.plot(x0,y0, label="kompressoimattomat pisteet")
plt.plot(x0,y1, label="kompressoidut pisteet")
#plt.yscale("log")
ax = plt.axes()
#ax.get_xaxis().set_visible(False)
#ax.tick_params(axis='x', )
#ax.yaxis.set_major_locator(MultipleLocator(5))
#ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))

#ax.xaxis.set_major_locator(MultipleLocator(5))
#ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))


plt.xlabel("ruutu")
plt.ylabel("ms")
plt.legend()
dir_path = os.path.dirname(os.path.realpath(__file__))
plt.savefig(os.path.join(dir_path, "..."))