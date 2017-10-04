#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 07:14:25 2017

@author: kaytemori
"""

 #Automate despotic GMC property finding to calculate the CO(1-0), CO(2-1) line
 #brightness ('intTb' in the despotic lines) and plot these brightnesses for
 #the despotic GMC model as a function of temperature for T= 5 K to 100 K
 #(T = 5, 10, 15, ... 100 K).
 
from despotic import cloud
import numpy as np
import matplotlib.pyplot as plt
 
gmc = cloud(fileName="MilkyWayGMC.desp", verbose=True)
gmc.setTempEq(verbose=True)

lines = gmc.lineLum("co")

T=np.linspace(5, 100, 20)

co10=np.zeros(T.size)
co21=np.zeros(T.size)

for i,temp in enumerate(T):
    gmc.Tg=temp
    lines = gmc.lineLum("co")
    co10[i]=lines[0]["intTB"]
    co21[i]=lines[1]["intTB"]
    
a1, = plt.plot(T,co10, 'ro', label='CO(1-0)')
a2, = plt.plot(T,co21, 'b+', label='CO(2-1)')
plt.title('Brightness of the CO(1-0) and CO(2-1) \n line emissions as a function of temperature',fontsize=14)
plt.xlabel('Tempurature (K)')
plt.ylabel('intTB (K km/s)')
plt.legend(handles = [a1,a2],loc = 'lower right')
plt.savefig('CO(1-0) and CO(2-1) line brightnesses.pdf')
plt.show()