import requests
import pandas as pd
from bs4 import BeautifulSoup
import math
import re
url = 'https://patoloco.com.br/produtos/placa-de-video'
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'}
 
site = requests.get(url, headers = headers)
soup = BeautifulSoup(site.content, 'html.parser')


dict_produtos = {'Marca': [], 'Preço_normal': []
, 'Preco_promocao':[], 'Desconto': []}

item = soup.find_all('article', class_ = 'product 1 clearfix')
contador = 1

for i in soup.find_all('h3', class_ = 'tit'):
    find_all_example = i.get_text()
    print(find_all_example)

## Incompleto