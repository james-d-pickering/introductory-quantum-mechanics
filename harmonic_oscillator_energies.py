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

ax = plt.gca()
v=0
m = 1
k = 1
hbar = 1
x = np.linspace(-4,4,400)
v = 0.5*k*(x**2)
E = np.arange(0,6,1)
Ev = E+0.5
for i in E:
    plt.plot([-np.sqrt(2*Ev[i]),np.sqrt(2*Ev[i])],[Ev[i],Ev[i]], label=r'v='+str(E[i]))
    
plt.plot(x, v, lw=2, color='k')
plt.annotate('',xy=(-1,Ev[1]), xytext=(-1,Ev[2]),color='k',arrowprops=dict(arrowstyle='<->'))
plt.text(-0.8, 2, r'$\hbar \omega', ha='center', va='center')
#plt.fill_between(x, y1=0, y2=v, alpha=0.8, color='xkcd:dark orange')
plt.xlim(-4,4)
plt.ylim(0,6)

handles, labels = ax.get_legend_handles_labels()
ax.legend(np.flipud(handles), np.flipud(labels))

plt.xticks([0])
plt.xlabel(r'$r-r_e$ [arb. units]')
plt.yticks([])

plt.ylabel(r'Energy [$\hbar \omega$]')
plt.savefig('harmonic_oscillator_energies.png',bbox_inches='tight',dpi=600)
