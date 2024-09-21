from urllib.request import urlopen

from urllib.error import HTTPError

from urllib.error import URLError

from bs4 import BeautifulSoup

try:

    html = urlopen("https://www.indiatoday.in/elections/delhi-assembly-polls-2020/story/delhi-assembly-election-2020-results-live-updates-vote-counting-news-aap-bjp-congress-1645172-2020-02-11")

except HTTPError as e:

    print(e)

except URLError:

    print("Server down or incorrect domain")

else:

    res = BeautifulSoup(html.read(), "html5lib")

    tags = res.findAll("div",{"class":"blog-multi-title"})


    for tag in tags:
        print(tag.getText())

