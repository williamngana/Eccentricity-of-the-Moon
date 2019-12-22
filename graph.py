# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 20:09:11 2018

@author: William James Ngana
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize as minz

## read file
def read_txt(fname):
    x = []
    y = []
    with open(fname) as f:
        lines_after_2 = f.readlines()[2:]
    for line in lines_after_2:
        data = line.split()
        x.append(float(data[0]))
        y.append(float(data[1]))
    return x, y

def x(x0,r,theta):
    return x0 + r*np.cos(theta)

def y(y0,r,theta):
    return y0 + r*np.sin(theta)


    
    


fname = "Neeb0320_2013.txt"
r = 600
x0 = 620
y0 = 700
xdata,ydata = read_txt(fname)
t = np.linspace(0,360,60)
xc = []
yc = []


for i in t:
    xc.append(x(x0,r,i))
    yc.append(y(y0,r,i))
def residual(guess):    
    a = [((x[0]-guess[1])**2 +(x[1]-guess[2])**2 - guess[0]**2)**2 for x in zip(xdata,ydata) ] 
    return sum(a)
initial_guess = [100, 620, 700] #[r,x0,y0]
result = minz(residual, initial_guess)
ans = result.x
xnew, ynew = [],[]
for i in t:
    xnew.append(x(ans[1],ans[0],i))
    ynew.append(y(ans[2],ans[0],i))
 

plt.errorbar(xdata, ydata, yerr=15, xerr=15, fmt = 'o')
plt.scatter(xdata, ydata)
#plt.scatter(xc,yc)
plt.plot(xnew,ynew, color = 'red')
plt.title('Apparent Size of the Moon')
plt.xlabel('X point as found in DS9')
plt.ylabel('Y point as found in DS9')
plt.show()
    