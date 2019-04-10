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
a = 1
x = np.linspace(-4,4,400)
v = (1-np.exp(-a*x))**2
E = np.arange(0,10,1)
v_dash = 1/(2*np.pi)
anh = v_dash/4
Ev = (E+0.5)*v_dash-((E+0.5)**2)*v_dash*anh
for i in E:
    plt.plot([-np.log(1+np.sqrt(Ev[i])),-np.log(1-np.sqrt(Ev[i]))],[Ev[i],Ev[i]], label=r'v='+str(E[i]))
    
plt.plot(x, v, lw=2, color='k')
#plt.annotate('',xy=(-1,Ev[1]), xytext=(-1,Ev[2]),color='k',arrowprops=dict(arrowstyle='<->'))
#plt.text(-0.8, 2, r'$\hbar \omega', ha='center', va='center')
#plt.fill_between(x, y1=0, y2=v, alpha=0.8, color='xkcd:dark orange')
plt.xlim(-2,4)
plt.ylim(0,1)
handles, labels = ax.get_legend_handles_labels()
ax.legend(np.flipud(handles), np.flipud(labels), loc=3)
plt.xticks([0])
plt.xlabel(r'$r-r_e$')
plt.yticks([])

plt.ylabel(r'Energy [$\hbar \omega$]')
plt.savefig('morse_potential.png',bbox_inches='tight',dpi=600)
