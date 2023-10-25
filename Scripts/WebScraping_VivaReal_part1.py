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
options.add_argument("'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'")

navegador = webdriver.Chrome(options=options)
navegador.get('https://www.vivareal.com.br/venda/minas-gerais/uberlandia/bairros/tubalina/lote-terreno_residencial/#onde=,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Tubalina,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ETubalina,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Cidade%20Jardim,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ECidade%20Jardim,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Nova%20Uberlandia,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ENova%20Uberlandia,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Patrim%C3%B4nio,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EPatrimonio,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Morada%20da%20Colina,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EMorada%20da%20Colina,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Vigilato%20Pereira,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EVigilato%20Pereira,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Saraiva,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ESaraiva,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Lagoinha,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ELagoinha,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Carajas,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ECarajas,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Pampulha,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EPampulha,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Jardim%20Kara%C3%ADba,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EJardim%20Karaiba,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Jardim%20Inconfid%C3%AAncia,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EJardim%20Inconfidencia,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Santa%20Luzia,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ESanta%20Luzia,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Granada,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EGranada,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,S%C3%A3o%20Jorge,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ESao%20Jorge,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Laranjeiras,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3ELaranjeiras,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Shopping%20Park,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EShopping%20Park,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,Jardim%20Sul,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EJardim%20Sul,,,;,Minas%20Gerais,Uberl%C3%A2ndia,Bairros,G%C3%A1vea,,,neighborhood,BR%3EMinas%20Gerais%3ENULL%3EUberlandia%3EBarrios%3EGavea,,,')
time.sleep(3)

lista_url = []


pages = True
while pages == True:
    try:    
        
        site = BeautifulSoup(navegador.page_source,'html.parser')
        time.sleep(5)
        
        imoveis = site.find_all('div',attrs={"data-type":"property"})

        for iv in imoveis:
           
            #Coleta Url imovel
            full_url = iv.find(class_='property-card__main-info').a.get('href')
            full_url = 'https://www.vivareal.com.br'+full_url
            url_iv = full_url

            lista_url.append(url_iv)
        
        

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
        navegador.execute_script("window.scrollTo(0, 9700)")
        time.sleep(1)
        receita.click()
    except:
        pages = False


#fecha o chromedriver
navegador.quit()



df = pd.DataFrame(lista_url,columns=['Url_imovel'])
df.to_csv('WebScrap_VivaReal1.csv',index=False)