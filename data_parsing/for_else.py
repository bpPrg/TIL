#!python
# -*- coding: utf-8 -*-#
"""
Config parser example

@author: Bhishan Poudel

@date: 

@email: bhishanpdl@gmail.com

"""
# Imports
import collections
from functools import partial
from collections import defaultdict
import os
from contextlib import contextmanager

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

def eg1():    
    for x in range(1,5):
        if x == 5:
            print ('find 5')
            break
    else:
        print ('can not find 5!')

def eg2():
    colors = ['red','green','blue','red','red']
    d = defaultdict(int)
    for color in colors:
        d[color] += 1

    print(d)

def eg3():
    colors = ['red','green','blue','pink','yellow']
    d = {}
    for color in colors:
        key = len(color)
        if key not in d:
            d[key] = []
        d[key].append(color)

    print(dict(d))

def eg4():
    colors = ['red','green','blue','pink','yellow']
    d = defaultdict(list)
    for color in colors:
        key = len(color)
        d[key].append(color)

    print(dict(d))

def eg5():
    d = collections.deque()
    d.extend('abcdefg')
    print("d = {}".format(d))
    
    d.append('h')
    print("d = {}".format(d))
    
    d.appendleft('h')
    print("d = {}".format(d))

def eg6():
    with ignored(OSError):
        os.remove('somefile.tmp')
    
def main():
    """Run main function."""
    eg6()

if __name__ == "__main__":
    main()
