#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 08:35:20 2019

@author: pickering
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


plt.rc('text', usetex=True)
plt.rc('font', family='sans-serif')

h = 6.626E-34
c = 3E8
temp = 5777
k = 1.38E-23
e = 1.6E-19
plt.close('all')


wavelength_nm = np.linspace(0,500,500)
energy_eV = 1240/wavelength_nm

wf_gold = 5.47
wf_silver = 4.74
wf_copper = 4.53

ke_gold = energy_eV-wf_gold
ke_silver = energy_eV-wf_silver
ke_copper = energy_eV-wf_copper

ke_gold[ke_gold<0]=0
ke_silver[ke_silver<0]=0
ke_copper[ke_copper<0]=0
   
plt.figure()

plt.plot(energy_eV,ke_gold, label=r'Gold')
plt.plot(energy_eV,ke_silver, label=r'Silver')
plt.plot(energy_eV,ke_copper, label=r'Copper')
plt.plot([wf_gold,wf_gold],[0,2],ls=":",alpha=0.5,color='k')
plt.plot([wf_silver,wf_silver],[0,2],ls=":",alpha=0.5,color='k')
plt.plot([wf_copper,wf_copper],[0,2],ls=":",alpha=0.5,color='k')
plt.text(wf_gold, 2.1, r'$\Phi_{\text{Au}}$',ha='center',va='center')
plt.text(wf_silver, 2.1, r'$\Phi_{\text{Ag}}$',ha='center',va='center')
plt.text(wf_copper, 2.1, r'$\Phi_{\text{Cu}}$',ha='center',va='center')

plt.ylim(0,2.5)
plt.xlim(4.25,6.25)
plt.xlabel(r'Incident Photon Energy [eV]')
plt.ylabel(r'$KE_{Elec.} [eV]')
plt.legend(fontsize=12)

plt.savefig('../final_figures/photoelectric.png',bbox_inches='tight',dpi=400)