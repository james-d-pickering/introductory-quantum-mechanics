#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:55:42 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
ax = plt.gca()

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
plt.plot(x, y, ls=':')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xticks((0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi),(r'0',r'\pi',r'2\pi',r'3\pi',r'4\pi'))
plt.yticks((-1,0,1))

plt.ylabel(r'$\sin(kL)$')
plt.xlabel(r'$kL$')
ax.xaxis.set_label_coords(1, 0.58)
plt.savefig('boundary_conditions_pinbox.png', bbox_inches='tight')