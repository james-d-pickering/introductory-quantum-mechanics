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

plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif',size='18')

plt.close('all')
plt.figure()

ax = plt.gca()
N = np.sqrt(2/0.7)
x = np.linspace(0.15,0.85,100)
wf_1 = 0.7*np.sin(np.pi*(x-0.15)/(0.7))
wf_2 = 0.7*np.sin(2*np.pi*(x-0.15)/0.7)
wf_3 = 0.7*np.sin(3*np.pi*(x-0.15)/0.7)

plt.plot(x, wf_1, label=r'n=1')
plt.plot(x, wf_2, label=r'n=2')
plt.plot(x, wf_3, label=r'n=3')
plt.legend(frameon=False, loc=(0.15,0))
wall1 = lines.Line2D([0.15,0.15],[-1,1],lw=1,color='k')
wall2 = lines.Line2D([0.85,0.85],[-1,1],lw=1,color='k')
ax.add_artist(wall1)
ax.add_artist(wall2)
axis3 = lines.Line2D([0,1],[0,0],lw=1,color='k')
ax.add_artist(axis3)
plt.xticks([0.15,0.85], [0, 'L'])
plt.yticks([-1,0,1])
plt.xlabel(r'$x$',labelpad=-10)
plt.ylabel(r'Wavefunction, $\Psi(x)$')
plt.xlim(0,1)
plt.ylim(-1,1)
ax.fill_between([0,0.15],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)
ax.fill_between([0.85,1],[-1,-1],[1,1],color='xkcd:dark orange',alpha=0.8)

plt.savefig('particle_in_box_wf.png',bbox_inches='tight')
