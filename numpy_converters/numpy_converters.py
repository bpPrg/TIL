#!python
# -*- coding: utf-8 -*-#
"""
Numpy loadtxt converter use

@author: Bhishan Poudel

@date: Feb 28, 2018

Ref: https://www.python-course.eu/numpy_reading_writing.php
https://www.python-course.eu/python3_generators.php

"""
# Imports
import numpy as np
import datetime
import time

def hms_to_seconds(t):
  if type(t) == bytes:
    t = t.decode()
    
  h, m, s = [int(i) for i in t.split(':')]
  return h*60 + m + s/60.0
    
    
for t in ["06:00:10", "06:27:45", "1:00:30"]:
    print(hms_to_seconds(t))


y = np.loadtxt("times_and_temperatures.txt", 
               converters={ 0: hms_to_seconds})
print(y)


# convert time to seconds
timestr = '00:04:23'
ftr = [3600,60,1]
secs = sum([a*b for a,b in zip(ftr, map(int,timestr.split(':')))])
print("secs = {}".format(secs))

# convert time to seconds
x = time.strptime('00:01:00','%H:%M:%S')
secs = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
print("secs = {}".format(secs))
