#!python
# -*- coding: utf-8 -*-#
"""
Nearest Points

@author: Bhishan Poudel

@date:  Dec 18, 2017

"""
# Imports
import numpy as np

a =[-1,3,50,60]
val = 25

l = max([ i for i in a if i < val])
u = min([ i for i in a if i >= val])

print(l,u)
