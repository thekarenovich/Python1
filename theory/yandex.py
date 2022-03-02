import requests
from bs4 import BeautifulSoup 

url = 'https://yandex.ru/'
page_yandex = requests.get(url)
soup = BeautifulSoup(page_yandex.text, 'html.parser')

all_a = soup.find_all("a")
for item in all_a:
	item_text = item.text
	# item_url = item.get('href')
	item_url = item['href']
	print(f'{item_text}: {item_url}')

