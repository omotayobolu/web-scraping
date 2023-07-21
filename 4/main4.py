from bs4 import BeautifulSoup
import requests

url = "https://eduprojecttopics.com/product-category/computer-sciences/"

html_text = requests.get(url).text
print(html_text)