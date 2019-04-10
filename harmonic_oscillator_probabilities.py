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
plt.rc('font', family='sans-serif',size='8')

plt.close('all')
fig = plt.figure()

fig.set_size_inches(8,8/3)
grid = gs.GridSpec(nrows=1, ncols=3)
ax = plt.subplot(grid[0,0])
v=0
m = 1
k = 1
hbar = 1
a = (m*k/(hbar**2))**0.25
N = (a/((2**v)*np.math.factorial(v)*np.sqrt(np.pi)))**0.5
H = 1
x = np.linspace(-5,5,2000)
wf_1 = N*H*np.exp(-((a*x)**2)/2)
v=3
N = (a/((2**v)*np.math.factorial(v)*np.sqrt(np.pi)))**0.5
H = (8*(a*x)**3)-12*a*x
wf_2 = N*H*np.exp(-((a*x)**2)/2)
v=5
N = (a/((2**v)*np.math.factorial(v)*np.sqrt(np.pi)))**0.5
#H = (256*((x*a)**8))-(3584*((x*a)**6))+(13440*((x*a)**4))+1680
H = (32*((x*a)**5))-(160*((x*a)**3))+(120*x*a)
wf_3 = N*H*np.exp(-((a*x)**2)/2)

plt.plot(x, wf_1**2, label=r'v=0')

#plt.plot(x, wf_3, label=r'v=2')
plt.grid()
plt.legend(frameon=True,loc=4)
#wall1 = lines.Line2D([0.15,0.15],[-1,1],lw=1,color='k')
#wall2 = lines.Line2D([0.85,0.85],[-1,1],lw=1,color='k')
#ax.add_artist(wall2)
#axis3 = lines.Line2D([0,1],[0,0],lw=1,color='k')
#ax.add_artist(axis3)


plt.xlabel(r'$x$',)
plt.ylabel(r'Probability Density, $\Psi^2(x)$')
ax.tick_params(axis='y',length=0)
x_v = np.linspace(-10,10,10000)
v = 0.5*0.03*x_v**2
plt.plot(x_v,v, alpha=0.7)
ax.set_yticklabels([])

plt.ylim(0,0.6)
plt.xlim(-10,10)
#ax.fill_between([0,0.15],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)
#ax.fill_between([0.85,1],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)

ax = plt.subplot(grid[0,1])
plt.plot(x, wf_2**2, label=r'v=3')
plt.xlabel(r'$x$')
plt.grid()
plt.ylim(0,0.35)
plt.xlim(-10,10)
ax.set_yticklabels([])
ax.tick_params(axis='y',length=0)
x_v = np.linspace(-10,10,10000)
v = 0.5*0.03*x_v**2
plt.plot(x_v,v, alpha=0.7)
#¤plt.plot(x, v)


plt.legend(loc=4)

ax = plt.subplot(grid[0,2])
plt.plot(x, wf_3**2, label=r'v=5')

plt.xlabel(r'$x$')
plt.grid()
plt.ylim(0)
plt.xlim(-10,10)
ax.tick_params(axis='y',length=0)
ax.set_yticklabels([])
x_v = np.linspace(-10,10,10000)
v = 0.5*0.03*x_v**2
plt.plot(x_v,v, alpha=0.7)


plt.legend(loc=4)

plt.savefig('harmonic_oscillator_probabilities.png',bbox_inches='tight',dpi=300)
