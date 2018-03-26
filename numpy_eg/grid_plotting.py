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
    x, y = np.arange(5), np.arange(5)
    distance = np.sqrt(x ** 2 + y[:, np.newaxis] ** 2)
    plt.pcolor(distance)
    plt.colorbar()
    plt.axis('equal')
    plt.show() 

def eg2():
    x, y = np.ogrid[0:5, 0:5]
    distance = np.sqrt(x ** 2 + y ** 2)
    plt.pcolor(distance)
    plt.colorbar()
    plt.axis('equal')
    plt.show() 
    print(x.shape, y.shape)

def eg3():
    x, y = np.mgrid[0:4, 0:4]
    print("x = {}".format(x))

def eg4():
    a = np.arange(36)
    b = a.reshape((6, -1))
    print('b = ', b) 

def main():
    """Run main function."""
    eg4()

if __name__ == "__main__":
    main()
