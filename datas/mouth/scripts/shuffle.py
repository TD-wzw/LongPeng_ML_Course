# _*_ coding:utf8 _*_
import os
import sys
import base64
import json
import math
import cv2
import random

def shuffle(file_in,file_out):
    fin = open(file_in,'r')
    fout = open(file_out,'w')

    lines = fin.readlines()
    random.shuffle(lines)
    for line in lines:
        fout.write(line)

shuffle(sys.argv[1],sys.argv[2])
