#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  18 19:40:59 2017

@author: kaytemori
"""
from despotic import cloud
import numpy as np
import scipy
from scipy.ndimage import map_coordinates as mc
def BuildDespoticInterpolator():
    gmc = cloud(fileName="MilkyWayGMC.desp", verbose=True)
    # gmc.setTempEq(verbose=True)

    lines = gmc.lineLum("co")

    T = np.linspace(10,20,5)
    logn = np.linspace(1,5,10)
    co10=np.zeros((T.size, logn.size))
    co21=np.zeros((T.size, logn.size))
    co32=np.zeros((T.size, logn.size))

    for j, density in enumerate(logn):
        for i,temp in enumerate(T):
            gmc.Tg=temp
            gmc.nH=1e1**density
            lines = gmc.lineLum("co")
            co10[i,j]=lines[0]["intTB"]
            co21[i,j]=lines[1]["intTB"]
            co32[i,j]=lines[2]["intTB"]
    fx = scipy.interpolate.interp1d(T,np.arange(len(T)))
    fy = scipy.interpolate.interp1d(logn,np.arange(len(logn)))

    def DespoticCO10(Tvals,n):
        intensity = mc(co10, [[fx(Tvals)],[fy(n)]])
        return(intensity)

    def DespoticCO21(Tvals,n):
        intensity = mc(co21, [[fx(Tvals)],[fy(n)]])
        return(intensity)

    def DespoticCO32(Tvals,n):
        intensity = mc(co32, [[fx(Tvals)],[fy(n)]])
        return(intensity)
    return(DespoticCO10,DespoticCO21,DespoticCO32)

#Do this with T and n as the full array
#Make the given plots
#T=np.array([10,10.1])
#
#n=np.array([2,2.1])
#
#f1(T,n)
#Out[46]: array([[ 77.09822974,  81.07471686]])
#
#f2(T,n)
#Out[47]: array([[ 54.05753451,  58.53544419]])
#
#f2(T,n)/f1(T,n)
#Out[49]: array([[ 0.70115144,  0.72199382]])
