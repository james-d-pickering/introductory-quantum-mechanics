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
fig.set_size_inches(8/3,16/3)
ax = plt.gca()
B = 1

js = np.arange(0,6,1)

for j in js:
    E = B*j*(j+1)
    plt.plot([0,1],[E,E],color='k')
    plt.text(1.2,E,r'J='+str(j),ha='center',va='center')
    
eng = B*js*(js+1)
eng_str = ['0B','2B','6B','12B','20B','30B']
plt.xticks([])
plt.yticks(eng,eng_str)
plt.ylabel(r'Energy (units of B)')
plt.savefig('rotational_energy_levels.png', bbox_inches='tight', dpi=200)
