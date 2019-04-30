#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:50:00 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif',size='12')

plt.close('all')
fig = plt.figure()
fig.set_size_inches(8,4)
grid = gs.GridSpec(1, 2, wspace=0.0)

ax = fig.add_subplot(grid[0,0],projection='3d')

r_ring = 1
theta_ring = np.linspace(0,2*np.pi,num=2000)

x_ring = r_ring*np.cos(theta_ring)
y_ring = r_ring*np.sin(theta_ring)
z_ring = np.ones_like(theta_ring)-1

r_wf = 1
N = 1/(np.sqrt(2*np.pi*r_wf))
m = 2
theta_wf_1 = N*(np.exp(theta_ring)+np.exp(-theta_ring))

x_wf_1 = r_wf*np.cos(theta_wf_1)
y_wf_1 = r_wf*np.sin(theta_wf_1)
z_wf_1 = r_wf*np.cos(theta_wf_1*m)

ax.plot3D(x_ring,y_ring,z_ring, color='k')
ax.scatter(x_wf_1, y_wf_1, z_wf_1,s=1,label=r'$\Psi_\text{Valid}$')
ax.set_zlim(-2,2)
ax.view_init(elev=15, azim=-56)
plt.axis('off')
#plt.legend()
ax.text(-1,-1,-2,'Single Valued - Acceptable')




ax = fig.add_subplot(grid[0,1],projection='3d')

r_ring = 1
theta_ring = np.linspace(0,2*np.pi,num=2000)

x_ring = r_ring*np.cos(theta_ring)
y_ring = r_ring*np.sin(theta_ring)
z_ring = np.ones_like(theta_ring)-1

r_wf = 1
N = 1/(np.sqrt(2*np.pi*r_wf))
m = 0
theta_wf_1 = N*(np.exp(theta_ring)+np.exp(-theta_ring))
ax.view_init(elev=15, azim=-56)

ax.set_zlim(-2,2)


theta_invalid = np.linspace(0,2*np.pi+0.4,num=2000)-np.pi/2
r_invalid = 1
wf_invalid = np.exp(theta_invalid)
z_invalid_f = np.linspace(0,1.3,num=2000)

x_invalid = r_invalid*np.cos(theta_invalid)
y_invalid = r_invalid*np.sin(theta_invalid)
z_invalid = (z_invalid_f)-0.5
ax.text(-1,-1,-2,'Multiple Values - Unacceptable')
#ax.scatter(-1.3,1,-1,marker="*",color='orange',s=40)
ax.plot3D([-1.3,-1.3,],[1,1],[-1.7,-0.3],ls="--",color='orange')
ax.scatter(x_invalid, y_invalid, z_invalid, color='r',s=1,label=r'$\Psi_\text{Invalid}')
ax.plot3D(x_ring,y_ring,z_ring, color='k')
plt.axis('off')
#plt.legend()
plt.savefig('../final_figures/rotational_wavefunctions.png',bbox_inches='tight',dpi=400)