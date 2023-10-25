import pandas as pd
import requests,time
from bs4 import BeautifulSoup
import numpy as np
import os

lista_apartamentos = pd.read_csv("Exel_and_Csv_Files\Viva_Real_Scrap 23-10-2023.csv",sep=',')

id_ap = lista_apartamentos['ID_VivaReal'].copy()
url_ap = lista_apartamentos['Url_Place'].copy()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
lista_imagens_apartamentos = []

parent_dir = "D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Imagens_Imoveis"
if(not os.path.exists(parent_dir)):
    os.mkdir(parent_dir)

for i in range(0,10):
    resposta = requests.get(url_ap[i],headers=headers)
    soup_mix = resposta.text
    soup = BeautifulSoup(soup_mix,'html.parser')
    imagens = soup.find_all('li',class_='carousel__slide js-carousel-item-wrapper')
    ap_img = []
    ap_img.append(id_ap[i])
    ap_img.append(url_ap[i])
    imgs = []


    directory = parent_dir +"\\"+ str(id_ap[i])
    if(not os.path.exists(directory)):
        os.mkdir(directory)

    contador = 1
    for img in imagens:
        url_img = img.find('img').get('src')
        url_img = url_img.replace("crop/142x80","fit-in/870x653")
        imgs.append(url_img)
        r = requests.get(url_img,headers=headers)
        time.sleep(1)
        with open(directory+f'\\foto{contador}.jpg','wb') as f:
            f.write(r.content)
        contador +=1    
    ap_img.append(imgs)
    
    lista_imagens_apartamentos.append(ap_img)


df = pd.DataFrame(lista_imagens_apartamentos)
df.to_csv('Exel_and_Csv_Files\VivaReal_Imagens_Imoveis.csv')
df.to_excel(r"Exel_and_Csv_Files\VivaReal_Imagens_Imoveis.xlsx")
