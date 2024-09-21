import requests
import lxml
from bs4 import BeautifulSoup

f=open('headline.txt','w')  # open a file -headlines.txt

SiteLink="https://www.bbc.com/news"
req=requests.get(SiteLink) # request to access  all data into -req
sup=BeautifulSoup(req.text,'html5lib')# to get all text in the link into- sup

nws=sup.find_all('h3',{'class':'gs-c-promo-heading__title'})    # to get  all h3 to -nws
for i in nws: # to get all h3 nd write into the file
    print(i.text)
    f.write(i.text)
    f.write('\n\n')
f.close()
print()

