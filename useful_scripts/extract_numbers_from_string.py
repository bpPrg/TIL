import os
import re
import glob
from natsort import natsorted

line = ' expdisk   : (  314.27,   306.99)   *23.93*     48.80    0.89   -34.97'

num_list = list(map(float, re.findall(r"""(?:-)?   # negative
                               \d+                 # digits
                               (?:\.\d+)?          # decimal part
                               """, line, re.X)))  # re.VERBOSE

print(num_list)
