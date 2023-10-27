import pandas as pd
import requests,time
from bs4 import BeautifulSoup
import numpy as np
from pathlib import Path

#Headers usado nos requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}


#Cria DataFrame com todas as informaçoes dos Imoveis
lista_apartamentos = pd.read_csv("D:\\ginga\\Documents\\Gustavo\\WebScraping_VivaReal\\WebScraping_VivaReal\\Exel_and_Csv_Files\\Viva_Real_Scrap 26-10-2023.csv",sep=',')

#Cria duas lista com infos que serão utilizadas mais a frente
id_ap = lista_apartamentos['ID_VivaReal'].copy()
url_ap = lista_apartamentos['Url_Place'].copy()

#Lista onde sera guardada as informacoes das fotos
lista_imagens_apartamentos = []

#Diretorio onde sera criada a pasta de fotos
parent_dir = Path().parent / 'Imagens_Imoveis'
parent_dir.mkdir(exist_ok=True)



for i in range(12,13):
    #Request da pagina do anuncio do imovel
    resposta = requests.get(url_ap[i],headers=headers)
    soup = BeautifulSoup(resposta.text,'html.parser')

    #Acha todas as tags que mostram as fotos
    imagens = soup.find_all('li',class_='carousel__slide js-carousel-item-wrapper')
    
    #lista para guardas infos do imovel e todos os paths das fotos
    ap_img = []
    ap_img.append(id_ap[i])
    ap_img.append(url_ap[i])
    
    #lista de paths das fotos
    imgs = []
    
    #Cria pasta para o imovel especifico
    directory = parent_dir / str(id_ap[i])
    directory.mkdir(exist_ok=True)

    contador = 1 #contador para ajudar no nomeamento das fotos

    for img in imagens: #Para cada tag/img na lista imagens
        url_img = img.find('img').get('src')                        #Acha a tag (img) e pega o conteudo de source
        url_img = url_img.replace("crop/142x80","fit-in/870x653")   #faz o tratamento necessario da string
                                                                    #faz um append na lista de urls
        
        #Download da Imagem
        #request da url da img
        r = requests.get(url_img,headers=headers)
        print(url_img)
        time.sleep(1)
        directory_imagem = directory / f'foto_{contador}_{id_ap[i]}.jpg'
        #Cria arquivo jpg e escreve conteudo do request nele
        with open(directory_imagem,'wb') as f:
            f.write(r.content)
        
        imgs.append(directory_imagem)
        contador +=1  #contador incrementa 1  
    ap_img.append(imgs)
    
    lista_imagens_apartamentos.append(ap_img)


#cria DF com todas as infos coletadas
df = pd.DataFrame(lista_imagens_apartamentos)
df.to_csv("Exel_and_Csv_Files\\VivaReal_Imagens_Imoveis.csv")
df.to_excel(r"Exel_and_Csv_Files\\VivaReal_Imagens_Imoveis.xlsx")
