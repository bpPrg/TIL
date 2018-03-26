#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : May 10, 2017 Wed
# Last update : Jun 19, 2017 Mon
# Est time    :
#
# Imports
import os
import glob
import re


# Rename filenames
def rename_files(idir,old,new):
    """ Rename all files in a folder.
    Arguments:
    Exmaples:
    idir = f814w_fitting/devauc_one_comp
    old  = f814w_devauc
    new  = f814w_devauc_one_comp
    
    """
    files = glob.glob(idir + '/' + old + '*.fits')
    for f in files:
        try:
            # f814w_fitting/devauc_one_comp/f814w_devauc0.fits
            f2 = f.replace(idir + '/' + old, idir + '/' + new)
            os.rename(f, f2)
            print("\n")
            print('From: ', f)
            print('To  : ', f2)
        except:
            pass

def main():
    # Devauc one comp
    idir = 'f814w_fitting/devauc_one_comp'
    old  = 'f814w_devauc'
    new  = 'f814w_devauc_one_comp'
    rename_files(idir,old,new)
    
    # Devauc two comp
    idir = 'f814w_fitting/devauc_two_comp'
    old  = 'f814w_devauc'
    new  = 'f814w_devauc_two_comp'
    rename_files(idir,old,new)
    
    # expdisk_res_one_comp
    idir = 'f814w_fitting/expdisk_res_one_comp'
    old  = 'f814w_expdisk_res'
    new  = 'f814w_expdisk_res_one_comp'
    rename_files(idir,old,new)
    
    # expdisk_res_two_comp
    idir = 'f814w_fitting/expdisk_res_two_comp'
    old  = 'f814w_expdisk_res'
    new  = 'f814w_expdisk_res_two_comp'
    rename_files(idir,old,new)
    
    # residual_two_comp
    idir = 'f814w_fitting/residual_two_comp'
    old  = 'f814w_res'
    new  = 'f814w_res_two_comp'
    rename_files(idir,old,new)


if __name__ == '__main__':
    main()
