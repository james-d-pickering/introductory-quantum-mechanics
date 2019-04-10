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
fig.set_size_inches(4,4)
r = np.linspace(0,2,num=200)
r_m = 0.5
e = 1

V_LJ = e*(((r_m/r)**12)-(2*(r_m/r)**6))

plt.plot(r, V_LJ)
plt.ylim(-1,1)
plt.xlim(0.25,1.5)
plt.xticks([0.5], [r'$r_m$'])
plt.yticks([0], [r'$E_0$'])
plt.plot([0,2],[0,0],ls=':',color='k',alpha=0.3)
plt.xlabel(r'Interatomic Separation, $r$')
plt.ylabel(r'Energy, $E$')

atom1 = patch.Circle((0.5,0.9),0.03, color='k')
atom2 = patch.Circle((0.58,0.9),0.03, color='k')

atom3 = patch.Circle((0.6,-0.9),0.03, color='k')
atom4 = patch.Circle((0.72,-0.9),0.03, color='k')

atom5 = patch.Circle((1.2,0.1),0.03, color='k')
atom6 = patch.Circle((1.45,0.1),0.03, color='k')

ax = plt.gca()
ax.set_aspect('equal')
ax.add_artist(atom1)
ax.add_artist(atom2)

ax.add_artist(atom3)
ax.add_artist(atom4)

ax.add_artist(atom5)
ax.add_artist(atom6)

plt.text(0.95,0.9,r'$r<r_m$, $E>E_0$',fontsize=8,ha='center',va='center')
plt.text(0.9,-0.8,r'$r=r_m$, $E<E_0$',fontsize=8,ha='center',va='center')
plt.text(1.2,0.2,r'$r>r_m$, $E=E_0$',fontsize=8,ha='center',va='center')

plt.savefig('PES.png', bbox_inches='tight', dpi=200)
