import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://indianexpress.com/page/3/?s=bjp').read()

soup = bs.BeautifulSoup(source,'lxml')

print(soup)

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)