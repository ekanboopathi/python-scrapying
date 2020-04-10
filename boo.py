from bs4 import BeautifulSoup
import urllib3

url = 'file:///C:/Users/Ekan%20Boopathi/Desktop/b.html'
html = urllib3.urlopen(url)
soup = BeautifulSoup(html)