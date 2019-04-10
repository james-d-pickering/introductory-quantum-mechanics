#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:50:00 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches

plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif',size='12')

plt.close('all')
fig = plt.figure()
fig.set_size_inches(8, 8/3)
grid = gs.GridSpec(1, 3, wspace=0.3)

f1_x = np.linspace(0,1,num=100)
f1_y = np.linspace(0,3,num=100)

f2_x = np.linspace(0,2,num=100)
f2_y = np.linspace(0,2,num=100)

f3_x = np.linspace(0,3,num=100)
f3_y = np.linspace(0,1,num=100)


ax = fig.add_subplot(grid[0,0])
#plt.plot(f1_x,f1_y)
arrowhead = mpatches.FancyArrowPatch((0,0),(1,3.05),mutation_scale=10,facecolor='k',arrowstyle='->')
ax.add_patch(arrowhead)
plt.xlim(0,4)
plt.ylim(0,4)
plt.xticks([0,1,2,3,4])
plt.yticks([0,1,2,3,4])
plt.plot([1,1],[0,3],ls=':')
plt.plot([0,1],[3,3],ls=':')
plt.xlabel(r'Component along $x$', color='C0')
plt.ylabel(r'Component along $y$', color='C1')
plt.grid()

ax = fig.add_subplot(grid[0,1])
arrowhead2 = mpatches.FancyArrowPatch((0,0),(2.05,2.05),mutation_scale=10,facecolor='k',arrowstyle='->')
ax.add_patch(arrowhead2)
#plt.plot(f2_x,f2_y)
plt.xlim(0,4)
plt.ylim(0,4)
plt.xticks([0,1,2,3,4])
plt.yticks([0,1,2,3,4])
plt.plot([2,2],[0,2],ls=':')
plt.plot([0,2],[2,2],ls=':')
plt.xlabel(r'Component along $x$', color='C0')
plt.ylabel(r'Component along $y$', color='C1')
plt.grid()

ax = fig.add_subplot(grid[0,2])
arrowhead3 = mpatches.FancyArrowPatch((0,0),(3.05,1),mutation_scale=10,facecolor='k',arrowstyle='->')
ax.add_patch(arrowhead3)
#plt.plot(f3_x,f3_y)
plt.xlim(0,4)
plt.ylim(0,4)
plt.xticks([0,1,2,3,4])
plt.yticks([0,1,2,3,4])
plt.plot([3,3],[0,1],ls=':')
plt.plot([0,3],[1,1],ls=':')
plt.xlabel(r'Component along $x$', color='C0')
plt.ylabel(r'Component along $y$', color='C1')
plt.grid()

plt.savefig('force_components.png',bbox_inches='tight',dpi=400)