#!python
# -*- coding: utf-8 -*-#
"""
Config parser example

@author: Bhishan Poudel

@date: 

@email: bhishanpdl@gmail.com

"""
# Imports
import sys
import os
from contextlib import contextmanager

@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = oldstdout
    

def eg2():
    with open('help.txt','w') as fo:
        with redirect_stdout(fo):
            help(pow)



def eg1():
    with ignored(OSError):
        os.remove('somefile.tmp')
    
def main():
    """Run main function."""
    eg2()

if __name__ == "__main__":
    main()
