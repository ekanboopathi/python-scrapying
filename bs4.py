import bs4 as bs
import requests
boo = requests.get('https://www.quora.com/topic/All-India-Anna-Dravida-Munnetra-Kazhagam-AIADMK-Indian-political-party')
type(boo)
soup = bs.BeautifulSoup(boo,'html.parser')

print(soup.body)