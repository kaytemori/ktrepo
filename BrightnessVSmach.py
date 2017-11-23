#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues Oct  31 09:37:40 2017

@author: kaytemori
"""

import numpy as np
import scipy.stats as ss
from DespoticInterpolator import BuildDespoticInterpolator
import matplotlib.pylab as plt

T = np.random.normal(18,3,1000)
#T = 15 * np.ones((1000))
sigma_ssq = 0.5
mean_density = 3e2

co10values,co21values,co32values = BuildDespoticInterpolator()

mach = np.logspace(0,3,31)

co10mean = np.zeros(len(mach))
co21mean = np.zeros(len(mach))
co32mean = np.zeros(len(mach))

for idx, m in enumerate(mach):
    mean_density = 3e2 * np.ones((1000))
    sigma_ssq = np.log((1 + m**2/4))
    densities = np.log10(mean_density * ss.lognorm.rvs(sigma_ssq, size=1000))
    co10 = co10values(T,densities)
    co10mean[idx] = np.mean(co10)
    co21 = co21values(T,densities)
    co21mean[idx] = np.mean(co21)
    co32 = co32values(T,densities)
    co32mean[idx] = np.mean(co32)


a1, = plt.semilogx(mach, co10mean, 'k', label='co10')
a2, = plt.semilogx(mach, co21mean, 'b', label='co21')
a3, = plt.semilogx(mach, co32mean, 'r', label='co32')
plt.legend()
plt.xlabel('Mach Number')
plt.ylabel('Line Brightness (K km/s)')
plt.title('Line Brightness as a Function of Mach Number')
plt.savefig('Line Brightness vs Mach Number.pdf')