from Arguments import *
import re

in_fp = open('text.txt')
out_fp = open('code.txt','w')
dicti = {}

for i in in_fp.read():
    if i in dicti:
        dicti[i]=dicti[i]+1
    else:
        dicti[i]=1

for i in range(256):
    char = chr(i+1)
    if char in dicti:
        out_fp.write(str(dicti[char]))
    else:
        out_fp.write('0')

    if i != 255:
        out_fp.write(',')

exit
