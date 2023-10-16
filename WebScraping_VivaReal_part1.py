import requests
from bs4 import BeautifulSoup
import time ,re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {'user-agent': 'Mozilla/5.0'}
options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=1366,768')


navegador = webdriver.Chrome(options=options)
navegador.get('https://www.vivareal.com.br/venda/minas-gerais/uberlandia/apartamento_residencial/#onde=Brasil,Minas%20Gerais,Uberl%C3%A2ndia,,,,,,BR%3EMinas%20Gerais%3ENULL%3EUberlandia,,,')


lista_imoveis = []


pages = True
while pages == True:
    try:    
        
        site = BeautifulSoup(navegador.page_source,'html.parser')
        time.sleep(5)
        
        imoveis = site.find_all('div',attrs={"data-type":"property"})

        for iv in imoveis:
            
            #Coleta id VivaReal
            if iv.get('id') is not None:   
                full_id = iv.get('id')
                id_iv = full_id
            else:
                full_id = iv.find('div',id = True).get('id')
                id_iv = full_id

            
            #Coleta Url imovel
            full_url = iv.find(class_='property-card__main-info').a.get('href')
            full_url = 'https://www.vivareal.com.br'+full_url
            url_iv = full_url

            
            #Coleta endereço e bairro
            full_endereco = iv.find('span',class_="property-card__address").text.strip()
            endereco = full_endereco.replace('\n', '')
            if full_endereco[:3]=='Rua' or full_endereco[:7]=='Avenida' or full_endereco[:8]=='Travessa' or full_endereco[:7]=='Alameda' or full_endereco[:5]=='Praça':
                bairro_1=full_endereco.strip().find('-')
                bairro_2=full_endereco.strip().find(',', bairro_1)
                if bairro_2!=-1:
                    bairro_text=full_endereco.strip()[bairro_1+2:bairro_2]
                    bairro = bairro_text # Guarde na lista todos os bairros
                else: # Bairro não encontrado
                    bairro_text='-'
                    bairro = bairro_text # Caso o bairro não seja encontrado
            else:
                get_comma=full_endereco.find(',')
                if get_comma!=-1:
                    bairro_text=full_endereco[:get_comma]
                    bairro = bairro_text # Guarde na lista todos os bairros com problema de formatação provenientes do proprio website  
                else:
                    get_hif=full_endereco.find('-')
                    bairro_text=full_endereco[:get_hif]
                    bairro = bairro_text


            #Coleta a area
            full_area=iv.find(class_="property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area").text.strip()
            area = full_area

            
            # Coleta titulo
            full_title = iv.find('span',class_='property-card__title js-cardLink js-card-title').text.strip()
            full_title = full_title.replace('\n','')
            title = full_title
            
            
            # Coleta numero de quartos
            full_quartos=iv.find(class_="property-card__detail-item property-card__detail-room js-property-detail-rooms").text.strip()
            full_quartos=full_quartos.replace(' ','')
            full_quartos=full_quartos.replace('\n','')
            full_quartos=full_quartos.replace('Quartos','')
            full_quartos=full_quartos.replace('Quarto','')
            quartos = full_quartos

            
            # Coleta numero de banheiros
            full_banheiros=iv.find(class_="property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom").text.strip()        
            full_banheiros=full_banheiros.replace(' ','')
            full_banheiros=full_banheiros.replace('\n','')
            full_banheiros=full_banheiros.replace('Banheiros','')
            full_banheiros=full_banheiros.replace('Banheiro','')
            banheiros = full_banheiros  

            
            # Coleta numero de vagas de garagem
            full_garagem=iv.find(class_="property-card__detail-item property-card__detail-garage js-property-detail-garages").text.strip()        
            full_garagem=full_garagem.replace(' ','')
            full_garagem=full_garagem.replace('\n','')
            full_garagem=full_garagem.replace('Vagas','')
            full_garagem=full_garagem.replace('Vaga','')
            garagens = full_garagem 

            
            #Coleta preço
            full_preco = re.sub('[^0-9]','',iv.find(class_="property-card__price js-property-card-prices js-property-card__price-small").text.strip())
            preco = full_preco

            #                       0     1    2   3    4     5        6     7      8        9     10     11    12  13  14  15  16  17    18               
            lista_imoveis.append([id_iv,preco,'-','-',title,bairro,endereco,area,quartos,banheiros,'-',garagens,'-','-','-','-','-','-',url_iv])


    except:
        print('Erro, 10 min para retomada')
        time.sleep(180)
        print('Erro, 7 min para retomada')
        time.sleep(120)
        print('Erro, 5 min para retomada')
        time.sleep(120)
        print('Erro, 3 min para retomada')
        time.sleep(60)
        print('Erro, 2 min para retomada')
        time.sleep(60)
        print('Erro, 1 min para retomada')
        time.sleep(60)


    #Muda de pagina
    try:
        receita = navegador.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')
        navegador.execute_script("window.scrollTo(0, 9250)")
        time.sleep(1)
        receita.click()
    except:
        pages = False


#fecha o chromedriver
navegador.quit()

#                                           0       1         2          3      4         5        6        7        8         9         10         11         12           13          14                  15                16             17            18                                           
df = pd.DataFrame(lista_imoveis,columns=['ID_VR','Preço','Condominio','IPTU','Titulo','Bairro','Endereco','Area','Quartos','Banheiros','Suites','Garagens','Anunciante','Telefone','Cod.Imobiliaria','Disponibilidade','Caracteristicas','Descrição','Url_Imovel'])
df =df.drop_duplicates()
df.to_csv('Exel_and_Csv_Files\Viva_Real_Scrap.csv',index=False)