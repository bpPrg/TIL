#!python
# -*- coding: utf-8 -*-#
"""
Numpy examples

@author: Bhishan Poudel

@date:  Nov 7, 2017

@email: bhishanpdl@gmail.com

"""
# Imports
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100)

def eg1():
    mean = [0, 0]
    cov = [[1, 0], [0, 10]]  # diagonal covariance

    x, y = np.random.multivariate_normal(mean, cov, size=5).T
    plt.plot(x, y, 'x')
    plt.xlim(-4,4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def main():
    """Run main function."""
    eg1()

if __name__ == "__main__":
    main()
