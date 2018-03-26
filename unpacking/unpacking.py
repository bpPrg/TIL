#!python
# -*- coding: utf-8 -*-#
"""
Python unpacking.   

@author: Bhishan Poudel

@date: Feb 18, 2018

"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

# eg1
a, = tuple([1])
z, = [3]
print(a)
print("z = {}".format(z))

# eg2
line, = plt.plot([1,2,3], [10,20,30], lw=2)
print("line = {}".format(line))

# eg 3
(a, b, c), (d, e, f), g = [[1,2,3], [4,5,6], [7,8,9]]
 
print("a = {}".format(a))
print("g = {}".format(g))
