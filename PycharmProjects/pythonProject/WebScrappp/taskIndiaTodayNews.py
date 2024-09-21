import requests
from bs4 import BeautifulSoup
import lxml

site="https://timesofindia.indiatimes.com/sports"

f=open("timesOfIndia.txt",'w')
req=requests.get(site)

sup=BeautifulSoup(req.text,'html5lib')

findClass=sup.findAll("span",{"class":"w_tle"})

for i in findClass:

    print(i.text)
    f.write(i.text)
    # f.write()
    f.write("\n")

