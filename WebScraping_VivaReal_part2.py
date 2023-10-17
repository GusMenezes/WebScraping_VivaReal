import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time ,re
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0'}
#options = Options()
#options.add_argument('--headless')
#options.add_argument('window-size=1366,768')

#Lista de Imoveis
lista_imoveis = pd.read_csv("Exel_and_Csv_Files\\Viva_Real_Scrap.csv",sep=',')

#Pega urls dos imoveis
lista_url = lista_imoveis['Url_Imovel'].copy()

#Posicoes a serem completadas na base
posicao = int(input('Posiçao inicial: '))


while posicao < len(lista_url):
    print(lista_url[posicao])
    
    #Coleta HTML site do imovel
    #navegador = webdriver.Chrome(options=options)
    #navegador.get(lista_url[posicao])
    #navegador.execute_script("window.scrollTo(0, 550)")
    #time.sleep(0.5)
    resposta = requests.get(lista_url[posicao],headers=headers)
    site_imovel = BeautifulSoup(resposta.text,'html.parser')


    print(posicao)
    try:           
        
        #imovel indisponivel ou disponivel
        if site_imovel.find('div',class_="inactive-udp__alert")is None:
            
            #Imovel Disponivel
            lista_imoveis.iat[posicao,15] = 'Disponivel'

            #Coleta nome anunciante
            full_anunciante = site_imovel.find('p',class_='legal__body')
            print(full_anunciante.contents[5].text)
            lista_imoveis.iat[posicao,12] = full_anunciante.contents[5].text

            #Condominio
            if site_imovel.find('span', class_='price__list-value condominium js-condominium') is not None:
                full_condominio = re.sub('[^0-9]','',site_imovel.find('span', class_='price__list-value condominium js-condominium').text.strip())
                lista_imoveis.iat[posicao,2] = full_condominio
            else:
                lista_imoveis.iat[posicao,2] = 'Não Informado'

            #Iptu
            if site_imovel.find('span', class_='price__list-value iptu js-iptu') is not None:
                full_iptu = re.sub('[^0-9]','',site_imovel.find('span', class_='price__list-value iptu js-iptu').text.strip())
                lista_imoveis.iat[posicao,3] = full_iptu
            else:
                lista_imoveis.iat[posicao,3] = 'Não Informado'

            #Suites
            if site_imovel.find('small',class_='features__extra-info') is not None:
                full_suites = site_imovel.find('small',class_='features__extra-info').text.strip()
                full_suites = full_suites.replace(' ','')
                full_suites = full_suites.replace('\n','')
                full_suites = full_suites.replace('suítes','')
                full_suites = full_suites.replace('suíte','')
                lista_imoveis.iat[posicao,10] = full_suites
            else:
                lista_imoveis.iat[posicao,10] = '-'


            #Coleta Descricao
            if site_imovel.find('p',class_ = 'description__text') is not None:
                full_descricao = site_imovel.find('p',class_ = 'description__text').text.strip()
                lista_imoveis.iat[posicao,17] = full_descricao

            #Coleta codigo imovel
            if site_imovel.find('span',class_='title__code js-external-id') != None:
                full_codigo = site_imovel.find('span',class_='title__code js-external-id').text.strip()
                full_codigo = full_codigo.replace('COD.','')
                full_codigo = full_codigo.replace(' ','')
                lista_imoveis.iat[posicao,14] = full_codigo
            
            #Coleta caracteristicas
            ul_aux = site_imovel.find('ul',class_='amenities__list')
            full_caracteristicas = []
            if ul_aux is not None:  #se apartamento tem caracteristicas, guarda na variavel
                caracteristicas_imovel = ul_aux.find_all('li')
                for c in caracteristicas_imovel:
                    x = c.text
                    full_caracteristicas.append(x)
            lista_imoveis.iat[posicao,16] = full_caracteristicas

            #Telefone
            #receita = navegador.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[2]/div[2]/div/aside/header/div/a')
            #receita.click()
            #time.sleep(1)
            
            url_anunciante = site_imovel.find(class_='publisher-details__name').a.get('href')
            url_anunciante = 'https://www.vivareal.com.br'+url_anunciante
            
            reposta = requests.get(url_anunciante,headers=headers)
            site_imovel = BeautifulSoup(resposta.text,'html.parser')
            
            full_telefone = site_imovel.find('div',class_='teaser__details-phone').text.strip()
            lista_imoveis.iat[posicao,13] = full_telefone
            

        else:
            #Imovel indisponivel
            lista_imoveis.iat[posicao,15] = 'Indisponivel'

        #Se nao deu erro, avança While
        posicao +=1
        #Salva cada apartamento em arquivo externo
        lista_imoveis.to_csv('Exel_and_Csv_Files\\Viva_Real_Scrap.csv',index=False)

    #Caso erro na busca, para 10 min e tente de novo.
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
    #navegador.quit()

lista_imoveis.to_excel(r'Exel_and_Csv_Files\Viva_real_Scrap.xlsx')