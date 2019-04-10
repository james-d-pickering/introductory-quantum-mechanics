#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:42:03 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.gridspec as gs
import matplotlib.patches as patch
from mpl_toolkits.mplot3d import Axes3D
from scipy import special

def sph2cart(r,theta,phi):
    x = r*np.cos(theta)*np.sin(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(phi)
    return x, y, z
    
plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif',size='12')

plt.close('all')
fig = plt.figure()
fig.set_size_inches(8.2, 8.2/4)
ax = fig.add_subplot(141,projection='3d')
ax1 = fig.add_subplot(142,projection='3d')
ax2 = fig.add_subplot(143,projection='3d')
ax3 = fig.add_subplot(144,projection='3d')

theta = np.linspace(0,2*np.pi,num=200)
phi = np.linspace(0,np.pi,num=100)
theta, phi = np.meshgrid(theta, phi)

Y00 = sp.special.sph_harm(0,0,theta,phi)
Y10 = sp.special.sph_harm(0,1,theta,phi)
Y20 = sp.special.sph_harm(0,2,theta,phi)
Y30 = sp.special.sph_harm(0,3,theta,phi)

Y00_x, Y00_y, Y00_z = sph2cart(np.abs(Y00), theta, phi)
Y10_x, Y10_y, Y10_z = sph2cart(np.abs(Y10), theta, phi)
Y20_x, Y20_y, Y20_z = sph2cart(np.abs(Y20), theta, phi)
Y30_x, Y30_y, Y30_z = sph2cart(np.abs(Y30), theta, phi)


ax.set_aspect('equal')
ax1.set_aspect('equal')
ax2.set_aspect('equal')
ax3.set_aspect('equal')

ax.plot_surface(Y00_x, Y00_y, Y00_z,color='deepskyblue')
ax1.plot_surface(Y10_x, Y10_y, Y10_z,color='deepskyblue')
ax2.plot_surface(Y20_x, Y20_y, Y20_z,color='deepskyblue')
ax3.plot_surface(Y30_x, Y30_y, Y30_z,color='deepskyblue')

ax.set_title(r'$Y_{00}(\theta, \phi)$')
ax1.set_title(r'$Y_{10}(\theta, \phi)$')
ax2.set_title(r'$Y_{20}(\theta, \phi)$')
ax3.set_title(r'$Y_{30}(\theta, \phi)$')

ax.text(0,0,-0.5,r'1s orbital',ha='center',va='center')
ax1.text(0,0,-0.85,r'2p orbital',ha='center',va='center')
ax2.text(0,0,-1.05,r'3d orbital',ha='center',va='center')
ax3.text(0,0,-1.2,r'4f orbital',ha='center',va='center')

ax.axis('off')
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')


plt.savefig('spherical_harmonics.png',bbox_inches='tight',dpi=300)

