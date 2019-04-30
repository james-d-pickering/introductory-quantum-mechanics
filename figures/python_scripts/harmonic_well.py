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
grid = gs.GridSpec(nrows=1,ncols=2, wspace=0.4)
x_force = np.linspace(0,1,100)
x_well = np.linspace(-2,2,400)
k1 = 1
k2 = 2
k3 = 0.5
force3 = k3*x_force
force2 = k2*x_force
force1 = k1*x_force
well1 = 0.5*k1*x_well*x_well
well2 = 0.5*k2*x_well*x_well
well3 = 0.5*k3*x_well*x_well

ax1 = plt.subplot(grid[0,0])
plt.plot(x_force, force1, label=r'$k_f=1$')
plt.plot(x_force, force2, label=r'$k_f=2$')
plt.plot(x_force, force3, label=r'$k_f=0.5')
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel(r'$x$ [m]')
plt.ylabel(r'abs($F_R$) [N]')
plt.legend(prop={'size':10})
ax1.text(0.5,1.05,r'(a)', va='center', ha='center')

ax2 = plt.subplot(grid[0,1])
plt.plot(x_well, well1,label=r'$k_f=1$')
plt.plot(x_well, well2,label=r'$k_f=2$')
plt.plot(x_well, well3,label=r'$k_f=0.5$')
plt.ylim(0,0.5)
plt.xlim(-1,1)
plt.xlabel(r'$x$ [m]')
plt.ylabel(r'$V(x)$ [J]')
ax2.text(0,0.525,r'(b)', va='center', ha='center')
plt.legend(prop={'size':10})


plt.savefig('harmonic_well.png', bbox_inches='tight', dpi=400)
