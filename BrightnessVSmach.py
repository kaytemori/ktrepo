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

T = 15
sigma_ssq = 0.5
mean_density = 3e2

densities = mean_density * ss.lognorm.rvs(sigma_ssq, size=1000)

co10values,co21values,co32values = BuildDespoticInterpolator()

co10values(T,densities)
co10average = np.mean(co10values)
co21values(T,densities)
co21average = np.mean(co21values)
co32values(T,densities)
co32average = np.mean(co32values)

mach = np.logspace(0,3,31)

a1, = plt.plot(mach, co10values, 'k', label='co10')
a2, = plt.plot(mach, co21values, 'b', label='co21')
a3, = plt.plot(mach, co32values, 'r', label='co32')
plt.legend(a1,a2,a3)
plt.xlabel('Mach Number')
plt.ylabel('Line Brightness')
plt.savefig('Line Brightness vs Mach Number.pdf')