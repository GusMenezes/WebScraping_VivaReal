import requests
import time ,re
import datetime
import mysql.connector
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

resposta = requests.get('https://www.vivareal.com.br/imovel/casa-de-condominio-3-quartos-varanda-sul-bairros-uberlandia-com-garagem-225m2-venda-RS1650000-id-2582740382/',headers=headers)
print('Status_Code=',resposta.status_code)

#HTML para pegar informacoes especificas
html = BeautifulSoup(resposta.text,'html.parser')


#Obtendo script desejado
soup = fromstring(resposta.text)
script = soup.xpath('/html/body/script[1]/text()')

#Tratamento do script para que possa ser trabalhado 
script = str(script[0])
js = script.split('/* Other data */\n      ...')
js = js[1].split('\n    };\n\n  function getSettings()')
js = js[0]


with open('script.json','w') as f:
    f.write(js)