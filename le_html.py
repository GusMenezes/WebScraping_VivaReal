import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

resposta = requests.get('https://www.vivareal.com.br/imovel/apartamento-2-quartos-tubalina-bairros-uberlandia-com-garagem-68m2-venda-RS480000-id-2660981065/',headers=headers)
site_imovel = BeautifulSoup(resposta.content,'html.parser')

file_html =  open('html.txt','w',encoding='utf-8')

file_html.write(str(site_imovel))

file_html.close()