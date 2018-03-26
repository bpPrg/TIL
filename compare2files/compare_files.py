#!python
# -*- coding: utf-8 -*-#
"""
compare two files.

@author: Bhishan Poudel

@date: Mar 12, 2018
https://unix.stackexchange.com/questions/45835/compare-two-files-lines-present-in-one-not-in-the-other-by-one-column-compari?rq=1

"""
# Imports


import sys

with open('b.txt') as f:
  file2col2 = {line.split()[1] for line in f}

with open('a.txt') as f:
  print("".join(line for line in f
                if line.split()[1] not in file2col2))


# with open(sys.argv[2]) as f:
#     file2col2 = {line.split()[1] for line in f}
# with open(sys.argv[1]) as f:
#     print("".join(line for line in f
#                   if line.split()[1] not in file2col2))


"""
join -1 2 -2 2 -v 1 <(sort a.txt) <(sort b.txt)

# a.txt
21  12340   3
21  12341   7
21  12342   2
21  12343   89
21  12349   7

#b.txt
21  12340   55
21  12341   7
21  12343   89
21  12344   7
21  12346   88
21  12347   3
21  12348   37

# answer
21  12342   2
21  12349   7



"""
