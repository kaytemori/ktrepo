#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 07:58:33 2017

@author: kaytemori
"""

def MySineWave(n):
    import matplotlib.pylab as plt
    import numpy as np
    x=np.linspace(-np.pi*2, np.pi*2, 200)
    plt.plot(x, np.sin((np.pi*2*x)/n))
    plt.show()
