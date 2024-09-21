import bs4
import requests

# Creating the requests

res = requests.get("https://en.wikipedia.org/wiki/Machine_learning")


# Convert the request object to the Beautiful Soup Object
soup = bs4.BeautifulSoup(res.text, 'html5lib')
soup.select('.mw-headline')
for i in soup.select('.mw-headline'):
    print(i.text,end = ',')
