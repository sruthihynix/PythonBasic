import bs4
import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.javatpoint.com/python-tutorial')
sup=bs4.BeautifulSoup(r.text,'html5lib')
sup.select('.h2')
f=open('jtp.txt','w')
for i in sup.select(('.h2')):
    print(i.text)
    f.write(i.text +'\n')