import bs4 as bs
import requests
boo = requests.get('https://www.instagram.com/explore/tags/bjp/')
type(boo)

soup = bs.BeautifulSoup(boo.text,'lxml')
type(soup)

for link in soup.find_all('a', href=True):
    print(link['href'])