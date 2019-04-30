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
plt.figure()
grid = gs.GridSpec(nrows=1, ncols=2)
ax = plt.subplot(grid[0,0])
v=0
m = 1
k = 1
hbar = 1
a = (m*k/(hbar**2))**0.25
N = (a/((2**v)*np.math.factorial(v)*np.sqrt(np.pi)))**0.5
H = 1
x = np.linspace(-4,4,400)
wf_1 = N*H*np.exp(-((a*x)**2)/2)
v=1
N = (a/((2**v)*np.math.factorial(v)*np.sqrt(np.pi)))**0.5
H = 2*x*a
wf_2 = N*H*np.exp(-((a*x)**2)/2)




#plt.plot(x, wf_3, label=r'v=2')
plt.grid()
plt.legend(frameon=True)
#wall1 = lines.Line2D([0.15,0.15],[-1,1],lw=1,color='k')
#wall2 = lines.Line2D([0.85,0.85],[-1,1],lw=1,color='k')
#ax.add_artist(wall2)
#axis3 = lines.Line2D([0,1],[0,0],lw=1,color='k')
#ax.add_artist(axis3)

ax = plt.subplot(grid[0,0])
plt.plot(x, wf_1, label=r'v=0')
plt.plot(x, wf_2, label=r'v=1')
plt.xlabel(r'$x = r-r_e$',)
plt.ylabel(r'Wavefunction, $\Psi(x)$')
plt.xlim(-4,4)
plt.ylim(-0.8,0.8)
plt.legend()
#ax.fill_between([0,0.15],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)
#ax.fill_between([0.85,1],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)

ax = plt.subplot(grid[0,1])
plt.plot(x, wf_1**2, label=r'v=1')
plt.plot(x, wf_2**2, label=r'v=2')
plt.ylabel(r'Probability Density, $\Psi^2(x)$')
plt.xlabel(r'$x = r-r_e$')
plt.grid()
ax.yaxis.set_label_position('right')
ax.yaxis.tick_right()
v = 0.5*k*(x**2)
v = v/np.max(v)
#¤plt.plot(x, v)
plt.xlim(-3,3)
plt.ylim(0,0.6)

plt.legend()



plt.savefig('../final_figures/harmonic_oscillator_wf.png',dpi=400,bbox_inches='tight')
