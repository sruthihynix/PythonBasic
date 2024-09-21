import  requests
from  bs4 import BeautifulSoup
website_url="https://infopark.in/companies/jobs"
keywords=["python",]

res=requests.get(website_url)
soup=BeautifulSoup(res.text,'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})
for job in jobs:
    title_element= job.find("a")
    title=title_element.text
    link=title_element["href"]
    company_name=job.find("div",{"class":"jobs-comp-name"}).text
    if any(word.lower() in  title.lower() for word in keywords):
        #print(title,company_name)

        dtls=title + " "+ company_name + " " + "\n" + link + "\n\n"
        print(dtls)
