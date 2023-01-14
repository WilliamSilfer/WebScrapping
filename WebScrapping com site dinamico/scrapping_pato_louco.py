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

num_itens = 204
ultima_pagina = math.ceil(int(num_itens) / 48)

dict_produtos = {'Marca': [], 'Preço_normal': []
, 'Preco_promocao':[], 'Desconto': []}

for i in range(1, ultima_pagina + 1):
    url_pages = f'https://patoloco.com.br/produtos/placa-de-video/{i}'
    site = requests.get(url_pages, headers = headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    
    item = soup.find_all('div', class_ = 'product-info')
    for i in item:
        marca = i.find('h3', class_ = 'tit').get_text().split()
        preco_normal = i.find('p', class_ = 'price-old').get_text().split()
        preco_promocao = i.find('p', class_ = 'price-new').get_text().split()

        print(f"Marca da placa: {marca} // Preço Normal: {preco_normal}, // Preço de promoção: {preco_promocao}")

## Filtrar algumas informações utilizando slince e adicionar no dicionário