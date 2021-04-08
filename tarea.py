import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

ua = UserAgent()
headers = {'user-agent':ua.chrome}
url = 'https://boston.craigslist.org/search/sof'

page = requests.get(url, headers = headers)
data = page.content

soup = BeautifulSoup(data, 'lxml')
lista_ofertas = soup.find_all('div', class_='result-info')

for lista in lista_ofertas:
    a = lista.find('a')
    print('Title: ', a.text)
    print('URL: ', a['href'])    

