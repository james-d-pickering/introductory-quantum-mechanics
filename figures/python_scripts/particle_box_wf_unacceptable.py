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
#plt.text(0.5,0.5, r'$V(x)=0$', ha='center', va='center')
#plt.text(0.125,0.5, r'$V(x)=\infty$', ha='center', va='center')
#plt.text(1-0.125,0.5, r'$V(x)=\infty$', ha='center', va='center')
#
#plt.text(0.5,0.4,r'Free Motion',ha='center',va='center')
#plt.text(0.125,0.4, r'Wall', ha='center', va='center')
#plt.text(1-0.125,0.4, r'Wall', ha='center', va='center')
x_box = np.linspace(0.25,0.75,50)
x_wall1 = np.linspace(0,0.25,25)
x_wall2 = np.linspace(0.75,1,25)
x_box_trig = ((x_box-0.25)/0.5)
plt.plot(x_box, 0.5*np.sin(np.pi*x_box_trig)+0.4, color='b')
plt.plot(x_wall1, 4*(x_wall1**2), color='b')
plt.plot(x_wall2, 4*np.flipud(x_wall1**2), color='b')
wall1 = lines.Line2D([0.25,0.25],[0,1],lw=1,color='k')
wall2 = lines.Line2D([0.75,0.75],[0,1],lw=1,color='k')
ax.add_artist(wall1)
ax.add_artist(wall2)
ax.annotate(r'Step = Unacceptable', xy=(0.25,0.35), xytext=(0.35,0.45),fontsize=12,arrowprops=dict(facecolor='black', shrink=0.05,width=1))
ax.annotate(r'Non-zero here = Unacceptable', xy=(0.8,0.15), xytext=(0.3,0.05),fontsize=12,arrowprops=dict(facecolor='black', shrink=0.05,width=1))

plt.xticks([0.25,0.75], [0, 'L'])
plt.yticks([0])
plt.xlabel(r'$x$',labelpad=-1)
plt.ylabel(r'Wavefunction $\Psi(x)$')
plt.xlim(0,1)
plt.ylim(0,1)
ax.fill_between([0,0.25],[0,0],[1,1],color='xkcd:dark orange',alpha=0.8)
ax.fill_between([0.75,1],[0,0],[1,1],color='xkcd:dark orange',alpha=0.8)

plt.savefig('particle_box_wf_unacceptable.png',bbox_inches='tight')
