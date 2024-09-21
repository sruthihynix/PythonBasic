from bs4 import BeautifulSoup
import requests
import lxml
url='https://infopark.in/companies/job-search'
res= requests.get(url)
soup=BeautifulSoup(res.text,"lxml")
jobs=soup.find_all("div",{"class":"row company-list joblist"})
# print(res.text)
for jobs in jobs:
    titleElement=jobs.find('a')
    title=titleElement.text
    link=titleElement['herf']
    print(title,link)
