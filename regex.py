# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:07:17 2020

@author: Gopal
"""

import re

fname = input("Enter the file name")
if len(fname)<1 : 
    fname = 'regex-2.txt'
fh = open(fname)
lst=[]
numlist=[]
for line in fh :
        
    lst =re.findall('[0-9]+',line)
    if len(lst) <1 : continue
    for i in range(len(lst)) :
        num = int(lst[i])
        numlist.append(num)
print(sum(numlist))

