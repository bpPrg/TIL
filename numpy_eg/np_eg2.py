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
    data = np.loadtxt('data/populations.txt')
    year, hares, lynxes, carrots = data.T 
    # plt.axes([0.2, 0.1, 0.5, 0.8])
    # plt.plot(year, hares, year, lynxes, year, carrots)
    # plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
    # plt.show()
    
    # population is data without year column
    # :, is all rows
    # 1: is all columns from 1 and excluding column 0.
    pop = data[:,1:]
    m = pop.mean(axis=0)
    print("m = {}".format(m))
    print("pop = {}".format(pop))

def main():
    """Run main function."""
    eg1()

if __name__ == "__main__":
    main()
