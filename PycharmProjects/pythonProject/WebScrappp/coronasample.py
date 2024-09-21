import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd

link='https://www.worldometers.info/coronavirus/country/india/'
r=requests.get(link)
sup=bs4.BeautifulSoup(r.text,'html5lib')

dataList=[]
case=sup.findAll("div",{"class":"maincounter-number"})
# print(case)
for i in case:
    span=i.find('span')
    print(span.string)
    dataList.append(span.string)
x=dataList[0]
print("Corina Virus Cases :",x)

