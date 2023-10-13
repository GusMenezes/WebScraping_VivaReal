import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time ,re
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0'}
proxylist = []

with open("proxy_list.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        proxylist.append(p)

#Lista de Imoveis
lista_imoveis = pd.read_csv("Exel_and_Csv_Files\Viva_Real_Scrap.csv",sep=',')

#Pega urls dos imoveis
lista_url = lista_imoveis['Url_imovel'].copy()

#Posicoes a serem completadas na base
posicao = int(input('Posiçao inicial: '))


while posicao < len(lista_url):
    print(lista_url[posicao])
    
    #Coleta HTML site do imovel
    for i in proxylist:    
        try:
            proxy = {
                'http': 'http://' + i,
                'https': 'http://' + i 
            }
            print(i)
            resposta = requests.get(lista_url[posicao],headers=headers,proxies=proxy,timeout=10)
            print(resposta.status_code)
            break
        except:
            pass
    
    site_imovel = BeautifulSoup(resposta.text,'html.parser')


    print(posicao)
    try:           
        
        #imovel indisponivel ou disponivel
        if site_imovel.find('div',class_="inactive-udp__alert")is None:
            

            #Coleta nome anunciante
            full_anunciante = site_imovel.find('p',class_='legal__body')
            print(full_anunciante.contents[5].text)



    #Caso erro na busca, para 10 min e tente de novo.
    except:
        print('Erro, 1 min para retomada')
        time.sleep(1)

