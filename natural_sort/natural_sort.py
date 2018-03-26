#!python
# -*- coding: utf-8 -*-#
"""
Sorting numbers naturally

@author: Bhishan Poudel

@date: Jan 25, 2018
https://stackoverflow.com/questions/4836710/does-python-have-a-built-in-function-for-string-natural-sort
"""
# Imports
import re
import natsort

def natural_sort(l): # natural sort with IGNORECASE
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key) 

    
def main():
    """Run main function."""
    l = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
    
    # non-natural sort
    # l2 = sorted(l)
    # print(l2)
    
    # using natsort
    # l2 = natsort.natsorted(l, key=lambda y: y.lower())
    # print(l2)
    
    # method
    # l2 = natural_sort(l)
    # print(l2)

if __name__ == "__main__":
    main()
