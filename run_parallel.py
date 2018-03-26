#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 19, 2017 Wed
# Last update :
#
# Imports
import numpy as np
import pandas as pd

def runInParallel(*fns):

    # import
    from multiprocessing import Process

    # processes
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

def main():
    """Main Module.
    """

    a = 332.907227
    b = a + 90
    print('b = ', b)     

if __name__ == '__main__':
    main()
