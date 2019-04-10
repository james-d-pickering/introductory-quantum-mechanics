#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:50:07 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.gridspec as gs
import matplotlib.patches as patch
plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif',size='12')

plt.close('all')
fig = plt.figure()
fig.set_size_inches(4,5)
ax = plt.gca()
plt.plot([0,1],[0.2,0.2], color='k')
plt.plot([0,1],[0.8,0.8], color='k')
plt.xlim(-0.5,1.5)
plt.ylim(0,1)
plt.xticks([])
plt.yticks([0.2,0.8],[r'$E_1$',r'$E_2'])
arrow = patch.FancyArrowPatch((0.1,0.2),(0.1,0.8),arrowstyle='simple',mutation_scale=20,color='b')
ax.add_artist(arrow)

arrow2 = patch.FancyArrowPatch((0.9,0.8),(0.9,0.2),arrowstyle='simple',mutation_scale=20,color='r')
ax.add_artist(arrow2)

plt.text(-0.2,0.25,r'Absorption',color='b',ha='center',va='center')
plt.text(1.2,0.25,r'Emission',color='r',ha='center',va='center')
plt.text(0.5,0.1,r'$\hbar\omega = \Delta E = E_2-E_1$',color='k',ha='center',va='center')

arrow3 = patch.FancyArrowPatch((0.4,0.2),(0.4,0.8),arrowstyle='|-|',mutation_scale=5,color='k',ls='-',alpha=0.5)
ax.add_artist(arrow3)
plt.text(0.5,0.5,r'$\hbar\omega$',color='k',ha='center',va='center')
plt.savefig('energy_gap.png', bbox_inches='tight', dpi=200)
