#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 09:35:25 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.gridspec as gs
plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif',size='12')

plt.close('all')
fig = plt.figure()
fig.set_size_inches(8,3)
grid = gs.GridSpec(1, 2, wspace=0.5)

ax = plt.subplot(grid[0,0])
#ax.set_aspect('1')
N = np.sqrt(2/0.7)
x = np.linspace(0.15,0.85,100)
wf_1 = 0.7*np.sin(np.pi*(x-0.15)/(0.7))
wf_2 = 0.7*np.sin(2*np.pi*(x-0.15)/0.7)
wf_3 = 0.7*np.sin(3*np.pi*(x-0.15)/0.7)

plt.plot(x, wf_1**2, label=r'n=1')
plt.plot(x, wf_2**2, label=r'n=2')
plt.plot(x, wf_3**2, label=r'n=3')
plt.legend(frameon=False, loc=(0.15,0.69))
wall1 = lines.Line2D([0.15,0.15],[-1,1],lw=1,color='k')
wall2 = lines.Line2D([0.85,0.85],[-1,1],lw=1,color='k')
ax.add_artist(wall1)
ax.add_artist(wall2)
axis3 = lines.Line2D([0,1],[0,0],lw=1,color='k')
ax.add_artist(axis3)
plt.xticks([0.15,0.85], [0, 'L'])
plt.yticks([0,1])
plt.xlabel(r'$x$',labelpad=-10)
plt.ylabel(r'Probability Density, $\Psi(x)^2$')
plt.xlim(0,1)
plt.ylim(0,1)
ax.fill_between([0,0.15],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)
ax.fill_between([0.85,1],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)

ax = plt.subplot(grid[0,1])
#ax.set_aspect('1')

N = np.sqrt(2/0.7)
x = np.linspace(0.15,0.85,1000)
wf_1 = 0.7*np.sin(100*np.pi*(x-0.15)/(0.7))


plt.plot(x, wf_1**2, label=r'n=100')

plt.legend(frameon=False, loc=(0.15,0.89))
wall1 = lines.Line2D([0.15,0.15],[-1,1],lw=1,color='k')
wall2 = lines.Line2D([0.85,0.85],[-1,1],lw=1,color='k')
ax.add_artist(wall1)
ax.add_artist(wall2)
axis3 = lines.Line2D([0,1],[0,0],lw=1,color='k')
ax.add_artist(axis3)
plt.xticks([0.15,0.85], [0, 'L'])
plt.yticks([0,1])
plt.xlabel(r'$x$',labelpad=-10)
plt.ylabel(r'Probability Density, $\Psi(x)^2$')
plt.xlim(0,1)
plt.ylim(0,1)
ax.fill_between([0,0.15],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)
ax.fill_between([0.85,1],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)
ax.fill_between([0.15,0.85],[0,0],[0.5,0.5])
plt.savefig('../final_figures/particle_in_box_probabilities.png', bbox_inches='tight', dpi=400)
