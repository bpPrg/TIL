#!python
# -*- coding: utf-8 -*-#
"""
Reading files

@author: Bhishan Poudel

@date:  Nov 7, 2017

@email: bhishanpdl@gmail.com

"""
# Imports
import numpy as np

x = np.array([1, 2, 3])
y = np.array([2,3,5])
z = np.array([2,3,4])

# mehhod 1
# xx,yy,zz = [a.reshape(a.shape[0],1) for a in (x,y,z) ]
# xyz = np.c_[xx,yy,zz]
# last = np.sum(xyz,axis=1)
# xyzz = np.c_[xyz,last.reshape(last.shape[0],1)]
# print(xyzz)

# method 2
xyz = np.stack((x,y,z),axis=-1)
last = np.sum(xyz,axis=1)
xyzz = np.c_[xyz,last[None:,]]
print(xyzz)
