# import bs4 as bs
# import requests
# boo = requests.get('https://www.quora.com/topic/All-India-Anna-Dravida-Munnetra-Kazhagam-AIADMK-Indian-political-party')
# type(boo)

# soup = bs.BeautifulSoup(boo.text,'lxml')
# type(soup)

# messages = [] 
# for i in soup.select('.ui_qtext_rendered_qtext'):
#     messages.append(i)

# count = 0

# print(len(messages))
# print(messages[9])

from requests import get
url = 'https://www.quora.com/topic/Dravida-Munnetra-Kazhagam-DMK'
response = get(url)
print(response.text[:500])