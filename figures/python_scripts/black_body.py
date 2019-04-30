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

plt.close('all')

sun_spectra = np.loadtxt('../data_files_for_figures/sun_black_body.txt')
wavelength_sun = np.loadtxt('../data_files_for_figures/sun_wavelengths.txt')
wavelength_nm = np.linspace(0,5000,500)
wavelength_m = wavelength_nm/1E9
frequency = c/wavelength_m
planck = (2*h*(c**2)/(wavelength_m**5))*(1/(np.exp((h*c)/(wavelength_m*k*temp))-1))


rayleigh = 2*c*k*temp/(wavelength_m**4)

plt.figure()
plt.plot(wavelength_nm, planck/1E13, label=r"Planck's Law")
plt.plot(wavelength_nm, rayleigh/1E13, label=r'Rayleigh-Jeans Law')
plt.plot(wavelength_sun, sun_spectra*1.25, linestyle="-", alpha=0.5, label=r'Solar Spectral Radiance')
plt.ylim(0,3)
plt.xlim(0,3000)
plt.xlabel(r'Wavelength [nm]')
plt.ylabel(r'Spectral Radiance [a.u.]')
plt.legend()

plt.savefig('../final_figures/black_body.png',dpi=400,bbox_inches='tight')