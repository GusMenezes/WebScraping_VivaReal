import requests
from bs4 import BeautifulSoup
import time ,re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

#Opções e Headers usados para requests
headers = {'user-agent': 'Mozilla/5.0'}
options = Options()
#options.add_argument('--headless')
options.add_argument('window-size=1366,768')
options.add_argument("'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'")

url_anuncios = 'https://www.vivareal.com.br/venda/minas-gerais/uberlandia/condominio_residencial/#onde=Brasil,Minas%20Gerais,Uberl%C3%A2ndia,,,,,,BR%3EMinas%20Gerais%3ENULL%3EUberlandia,,,&preco-desde=1000000'


#Abre Navegador com Selenium
navegador = webdriver.Chrome(options=options)
navegador.get(url_anuncios)
time.sleep(3)


lista_url = []  #Lista para guardar todos links de cada Imovel


pages = True   #Enquanto verdadeiro, existe pagina seguinte
while pages == True:
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


    #Muda de pagina
    try:
        receita = navegador.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')
        navegador.execute_script("arguments[0].scrollIntoView(true);", receita)
        time.sleep(0.5)
        receita.click()

    except Exception as e:
        print(e)
        pages = False


#fecha o chromedriver
navegador.quit()



df = pd.DataFrame(lista_url,columns=['Url_imovel'])
df.to_csv("D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Exel_and_Csv_Files\LISTA_URLS_VIVAREAL.csv",index=False)