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
fig = plt.figure()
fig.set_size_inches(3,6)
l = 2
ml = np.arange(-2,3,1)

theta = np.arccos(ml/(np.sqrt(l*(l+1))))

y = np.sqrt(l*(l+1))*np.cos(theta)
x = np.sqrt(l*(l+1))*np.sin(theta)

for i in ml:
    plt.plot([0,x[i]],[0,y[i]],color='k')
    plt.plot([0,x[i]],[y[i],y[i]],color='k',alpha=0.5,ls=':')
plt.ylabel(r'$m_l$')
plt.yticks([-2,-1,0,1,2])   
plt.xticks([]) 
plt.xlim(0,)
plt.text(2.2,0.2,r'$|l|$',ha='center',va='center')
plt.savefig('vector_model.png', bbox_inches='tight',dpi=300)