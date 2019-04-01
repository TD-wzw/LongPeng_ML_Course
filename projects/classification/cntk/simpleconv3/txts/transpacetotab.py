import os
import sys
fin=open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
lines = fin.readlines()
for line in lines:
    line = line.replace(' ','\t')
    fout.write(line)
