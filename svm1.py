# -*- coding: utf-8 -*-
"""
Created on Sat May 07 09:34:27 2016

@author: kamal
"""

'''
mylist=["a","b","c","d"]
for i,j in enumerate(mylist):
    print i,j
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
np.random.seed(1)
n_samples = 150
X = datasets.make_circles(n_samples=n_samples, factor=.25,
                                      noise=.05)
X_val=X[0]                                      
label=X[1]

uniq=np.unique(label)
color=['ro','bo']
for i in range(2):
    index=label==uniq[i]
    plt.plot(X_val[index,0],X_val[index,1],color[i])
plt.show()    
    
z1=X_val[:,0]
z11=z1**2
z2=X_val[:,1]
z22=z2**2
z3=np.sqrt(2)*z11*z22

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(z11, z22,z3,c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

newfeat=(1*np.ones(150)+z2.T*z1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(z11, z22, newfeat,c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')