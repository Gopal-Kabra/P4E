# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 00:19:57 2020

@author: Gopal
"""

import urllib
from bs4 import BeautifulSoup

url = input("enter the url:")
count = int(input("enter the Count for loop"))
position = int(input("enter the position"))
if len(url)<1 :
    url = "http://py4e-data.dr-chuck.net/known_by_Leyton.html"

for i in range(count):

    htmV = urllib.request.urlopen(url)
    sup = BeautifulSoup(htmV , "html.parser")
    #print(sup)
    Atag = sup('a')
    #print(Atag)

    for A in Atag[position-1:position]:
        temp = A.contents[0]
        url =A.get('href')
        #print(temp , url)
    
print(temp)
