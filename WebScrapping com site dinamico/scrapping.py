import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  \
                         (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"}
site = requests.get(url, headers= headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', id = 'listingCount').get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]
ultima_pagina = math.ceil(int(qtd)/20)

dict_produtos =  {'marca':[], 'preco':[]}

for i in range(1, ultima_pagina + 1):
    url_pages = f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pages, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_= re.compile('productCard'))

    for produto in produtos:
        marca = produto.find('span', class_= re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_= re.compile('priceCard')).get_text().strip()

        dict_produtos['marca'].append(marca)
        dict_produtos['preco'].append(preco)

print(dict_produtos['marca'][:1], dict_produtos['preco'][:1])
df = pd.DataFrame(dict_produtos)
df.to_csv('C:/Users/walli/Documents/WebScrapping/WebScrapping com site dinamico/lista_cadeiras.csv', encoding='utf-8', sep= ';')