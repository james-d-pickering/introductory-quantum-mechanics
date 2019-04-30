#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:47:35 2019

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

n = np.arange(1, 8, 1)

E = n**2
for i in n:
    plt.plot([0,1],[E[i-1],E[i-1]], color='b')
    plt.text(1.2, E[i-1], 'n='+str(i), ha='center', va='center')


plt.xlim(0,1.4)
plt.xticks([])
plt.yticks([0])
plt.ylabel(r'Energy/$(h^2/8mL^2)$')
ax.set_aspect(aspect=0.05)
plt.savefig('../final_figures/particle_in_box_energies.png', dpi=400,bbox_inches='tight')