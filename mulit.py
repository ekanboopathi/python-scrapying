import bs4
import requests
res = requests.get("https://www.quora.com/topic/All-India-Anna-Dravida-Munnetra-Kazhagam-AIADMK-Indian-political-party")
type(res)
soup = bs4.BeautifulSoup(res.text,'lxml')
type(soup)