# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:29:04 2020

@author: Gopal
"""

import urllib
import xml.etree.ElementTree as ET

sum = 0
url = input("ENter the Url-  :  ")
if len(url)<1 :
    url='http://py4e-data.dr-chuck.net/comments_814257.xml'
    
fh = urllib.request.urlopen(url)
data = fh.read()
#print(data)    
tree = ET.fromstring(data)
lst = tree.findall('.//count')
#print(len(lst))
for  item in lst:
    sum = sum + int(item.text)
    
print(sum)