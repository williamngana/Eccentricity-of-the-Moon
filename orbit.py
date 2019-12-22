# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 15:22:22 2018

@author: William James Ngana
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize as minz

day =[23.21,20.22,21.24]
ang_pos=[303.29,264.22,277.55]

xpoints = [ x[0]*np.cos(np.deg2rad(x[1])) for x in zip(day,ang_pos)]
ypoints = [ x[0]*np.sin(np.deg2rad(x[1])) for x in zip(day,ang_pos)]
t = np.linspace(0,360,60)



def x(a,theta):
    return a*np.cos(theta)

def y(b,theta):
    return b*np.sin(theta)

def residual(guess):    
    a = [((x[0]/guess[0])**2 +(x[1]/guess[1])**2 - 1)**2 for x in zip(xpoints,ypoints) ] 
    return sum(a)
initial_guess = [100, 200] #[a,b]
result = minz(residual, initial_guess)
ans = result.x
xnew, ynew = [],[]
for i in t:
    xnew.append(x(ans[0],i))
    ynew.append(y(ans[1],i))

plt.scatter(xpoints,ypoints)    
plt.plot(xnew,ynew, color = 'red')
plt.title('Orbit of the Moon')
plt.xlabel('X Poistion')
plt.ylabel('Y Poistion')
plt.show()