import nltk
from newspaper import Article
url = 'https://www.quora.com/'
article = Article(url)
article.download()