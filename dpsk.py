# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:44:29 2019

@author: Saif
"""

import numpy as np
import matplotlib.pyplot as plt

n = 100
b = np.round(np.random.rand(n,))
x = np.zeros((n,))
v = x
rb = 10
tb = 1/rb
fs = 5*rb
ts = 1/fs
fc = 10000

for i in range(2,n):
    x[i] = 1 - (x[i-1] != b[i])
    
v[x == 1] = 5
v[x == 0] = -5
t = np.linspace(0 , 10*tb , 100*tb/ts)
m = np.zeros((len(t),))
c = np.cos(2*np.pi*fc*t)

for j in range(len(t)):
    for k in range(0,len(v)-1):
        if (t[j] > k*tb) & (t[j] <= (k+1)*tb):
            m[j] = v[k+1]
            

y = c*m

plt.plot(t,m , 'r') 

plt.savefig('plot1')       


