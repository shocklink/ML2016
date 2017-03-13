#!/usr/bin/python


import os
import sys

filaname = sys.argv[2]
colume = int(sys.argv[1])

alist = []
with open(filaname, 'r') as f:
    for line in f:
        word = line.split()
        alist.append(word[colume])
    print sorted(alist, key = lambda x: (float(x)))
