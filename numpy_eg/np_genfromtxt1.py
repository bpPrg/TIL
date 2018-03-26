#!python
# -*- coding: utf-8 -*-#
"""
Reading string bounded floats.

@author: Bhishan Poudel

@date: Feb 10, 2018

https://exceptionshub.com/python-3-5-typeerror-a-bytes-like-object-is-required-not-str-when-writing-to-a-file.html
"""
# Imports
import numpy as np


convert = lambda x:  float(x.decode('utf8').strip('"'))


data = np.genfromtxt('data/string_data.txt',delimiter=',',skip_header=2,converters={0: convert,1: convert,2: convert,3: convert,4: convert},dtype=None)

print("data = {}".format(data))
