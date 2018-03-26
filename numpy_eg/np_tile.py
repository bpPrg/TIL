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
    a = np.tile(np.arange(0, 40, 10), (3, 1)).T
    b = np.array([0, 1, 2])
    print('a = ', a)
    print('b = ', b)
    print("a+b = {}".format(a+b))

def eg2():
    a = np.arange(0,40,10)
    b = np.array([0, 1, 2])
    # print("a.shape = {}".format(a.shape)) # (4,)
    
    # make column vector
    a = a[:, np.newaxis]
    # print("a.shape = {}".format(a.shape)) # (4,1)
    print("a+b = {}".format(a+b))

def main():
    """Run main function."""
    eg2()

if __name__ == "__main__":
    main()
