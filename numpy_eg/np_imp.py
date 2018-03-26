#!python
# -*- coding: utf-8 -*-#
"""
Numpy examples

@author: Bhishan Poudel

@date:  Nov 7, 2017

@email: bhishanpdl@gmail.com

http://www.scipy-lectures.org/intro/numpy/numpy.html
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

def eg1():
    a = np.array([1,2,3])
    print("a.dtype = {}".format(a.dtype))
    a[0] = 1.9  # <-- float is truncated to integer
    print('a = ', a)
    
    # to make float array
    a = a.astype(float)
    a[0] = 1.9
    print('a = ', a)

def main():
    """Run main function."""
    eg1()

if __name__ == "__main__":
    main()
