import requests
import pandas as pd
from bs4 import BeautifulSoup
import math
import re

url = 'https://www.pichau.com.br/hardware/placa-de-video'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0'}

site = requests.get(url, headers = headers)
soup = BeautifulSoup(site.content, 'html.parser')



# Por não conseguir coletar o número dos produtos, fica aqui a atualização manual
qtd_produtos = 1728 
ultima_pagina = math.ceil(int(qtd_produtos)/ 36)

dict_produtos = {'Marca':[], 'Preco':[], 'Preco Boleto':[]}

for i in range(1, ultima_pagina+1):
    url_page = f'https://www.pichau.com.br/hardware/placa-de-video?page={i}'
    site = requests.get(url_page, headers = headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    placas = soup.find_all('div', class_= re.compile('MuiCardContent-root'))
    for j in placas:
        marca = j.find('h2', class_=re.compile('MuiTypography-root')).get_text().strip()

        try:
            preco = j.find('div', class_='jss87').get_text().strip()[2:]
        except:
            preco = '0'
        try:
            preco_boleto = j.find('div', class_ ='jss79').get_text().strip()[2:]
            index = preco_boleto.find(',')
            num_preco_boleto = preco_boleto[10:index]
        except:
            preco_boleto = '0'


        dict_produtos['Marca'].append(marca)
        dict_produtos['Preco Boleto'].append(preco_boleto)
        dict_produtos['Preco'].append(preco)
        print(marca, preco, preco_boleto)

df = pd.DataFrame(dict_produtos)
df.to_csv('C:/Users/walli/Documents/GitHub/Scripts-Python/WebScrapping com site dinamico/lista_placas_video_pichau.csv', encoding='utf-8', sep= ';')
