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


def main():
    x = np.array([
       [1,  1],
       [1,  2],
       [5,  1],
       [3,  2]])
       
    b = np.sum(x**2, axis=1, keepdims=True)
    
    c = np.concatenate([x,b],axis=1)
    # print(x)
    print('b = ', b)
    print('c = ', c) 
    
    # just the sum
    b_sum = np.sum(x**2,axis=1).sum()
    b_sum2 = np.sum(b)
    print("b_sum, b_sum2 = {}, {}".format(b_sum,b_sum2))

if __name__ == "__main__":
    main()        
