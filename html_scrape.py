# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:37:06 2020

@author: Gopal
"""
import urllib
from bs4 import BeautifulSoup

url = input("Enter - url")
if len(url)<1 :
    url =' http://py4e-data.dr-chuck.net/comments_814255.html'
 
total=0    
htmV = urllib.request.urlopen(url).read()
#print(htmV)
neat = BeautifulSoup(htmV,'html.parser')
#print(neat)

spans = neat('span')
#print(spans)
for num in spans:
    total = total + int(num.contents[0])
print(total)
