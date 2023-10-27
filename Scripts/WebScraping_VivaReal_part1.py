import requests
from bs4 import BeautifulSoup
import time ,re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Opções e Headers usados para requests
headers = {'user-agent': 'Mozilla/5.0'}
options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=1366,768')
options.add_argument("'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'")

url_anuncios = 'https://www.vivareal.com.br/venda/minas-gerais/uberlandia/granja_comercial/#onde=,Minas%20Gerais,Uberl%C3%A2ndia,,,,,city,BR%3EMinas%20Gerais%3ENULL%3EUberlandia,-19.038245,-47.916014,&itl_id=1000183&itl_name=vivareal_-_botao-cta_buscar_to_vivareal_resultado-pesquisa'


#Abre Navegador com Selenium
navegador = webdriver.Chrome(options=options)
navegador.get(url_anuncios)
time.sleep(3)


lista_url = []  #Lista para guardar todos links de cada Imovel


pages = 0   #Enquanto verdadeiro, existe pagina seguinte
while pages <= 5:
    try:     
        #Pega o html fatorado
        site = BeautifulSoup(navegador.page_source,'html.parser')
        time.sleep(5)
        
        #Pega todas as tags que contem as urls desejadas
        imoveis = site.find_all('div',attrs={"data-type":"property"})

        for iv in imoveis: #for 
           
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

    pages +=1
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
df.to_csv("D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Exel_and_Csv_Files\LISTA_URLS_VIVAREAL.csv",index=False)