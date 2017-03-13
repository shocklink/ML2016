#!/usr/bin/python

import os
import sys
from PIL import Image


imagename = sys.argv[1]

raw_im = Image.open(imagename)
print (raw_im.format)

im = raw_im.convert('RGB')
w, h = im.size
data = im.getdata()
r, g, b = im.getpixel((w-1,h-1))

print w, h
print data
print r, g, b

new_im = Image.new("RGB", (w, h), "white")
for y in range(0, h-1):
    for x in range(0, w-1):
        r, g, b = im.getpixel((x,y))
        new_im.putpixel((w-x-1,h-y-1), (r, g, b))
        #print r,g,b

new_im.save("ans2.png")
