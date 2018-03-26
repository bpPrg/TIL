#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 04, 2017 Tue
# Last update : 
#
# Imports
import time
import os
import subprocess

if os.path.isfile('conf.py'):
    subprocess.call('mv conf.py conf2.py', shell=True)




with open('conf2.py', 'r') as f, open('conf.py','w') as fo:
    for line in f.readlines():
        olds = [r'# import os', 
                r'# import sys',
                r"# sys.path.insert(0, os.path.abspath('.'))",
                r"html_theme = 'alabaster'"]
        news = [r'import os', 
                r'import sys',
                r"sys.path.append('../scripts/')",
                r"html_theme = 'default'"]
        if olds[0] in line:
            print(line.replace(olds[0], news[0]), file=fo, end='')
        elif olds[1] in line:
            print(line.replace(olds[1], news[1]), file=fo, end='')
        elif olds[2] in line:
            print(line.lstrip('#').lstrip(' '), file=fo, end='')
            print(news[2], file=fo, end='')
        elif olds[3] in line:
            print(line.replace(olds[3], news[3]), file=fo, end='')
        else:
            print(line, file=fo, end='')
            

os.remove('conf2.py')
