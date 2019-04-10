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
import matplotlib.image as mpimg
plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif',size='12')

plt.close('all')
fig = plt.figure()

grid = gs.GridSpec(1, 2, wspace=0.1)

ax = plt.subplot(grid[0,0])
image = mpimg.imread('angular_momentum_small.png') 
plt.imshow(image)
ax.text(900,0.5,r'(a)')
plt.axis('off')
ax = plt.subplot(grid[0,1])
image = mpimg.imread('angular_momentum_large.png') 
plt.imshow(image)
ax.text(1350,0.5,r'(b)')

plt.axis('off')
plt.savefig('angular_momenta.png', bbox_inches='tight', dpi=400)
