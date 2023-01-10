import requests
import pandas as pd
from bs4 import BeautifulSoup
import math
import re

url = 'https://www.pichau.com.br/hardware/placa-de-video'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'}

site = requests.get(url, headers = headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_= re.compile('MuiCardContent-root'))


# Por não conseguir coletar o número dos produtos, fica aqui a atualização manual
qtd_produtos = 1728 
ultima_pagina = math.ceil(int(qtd_produtos)/ 36)


for i in range(1, ultima_pagina+1):
    print(i)

placas = placas[0]


marca = placas.find('h2', class_=re.compile('MuiTypography-root')).get_text().strip()
preco = placas.find('div', class_='jss87').get_text().strip()[2:][:-3]

preco_boleto = placas.find('div', class_ ='jss79').get_text().strip()[2:][:-3]
#print(f'Preco boleto: {preco_boleto}, Preco normal {preco}')
