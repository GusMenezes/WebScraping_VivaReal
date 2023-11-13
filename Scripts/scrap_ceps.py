import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

respostas= requests.get("https://codigo-postal.org/pt-br/brasil/mg/uberlandia/",headers=headers)
soup=BeautifulSoup(respostas.text,"html.parser")

aux_ul=soup.find("ul",class_="column-list")

lista_regioes = aux_ul.find_all("a")
lista_CEP=[]

for x in lista_regioes:
    try:
        respostas= requests.get(x.get('href'),headers=headers)
        print(respostas.status_code)
        soup=BeautifulSoup(respostas.text,"html.parser")

        aux_tbory = soup.find("tbody",id="tbody_results_")

        lista_tr = aux_tbory.find_all("tr")
        for y in lista_tr:
            cep = []
            lista_td = y.find_all("td")


            if lista_td[0].a.text == 'ver todos':
                respostas = requests.get('https://codigo-postal.org/'+lista_td[0].find(class_="btn btn-xs btn-primary").get('href'),headers=headers)
                print(respostas.status_code)
                soup = BeautifulSoup(respostas.text,'html.parser')
                ver_todos_tbody = soup.find("tbody",id="tbody_results_")
                ver_todos_tr = ver_todos_tbody.find_all("tr")

                for i in ver_todos_tr:
                    cep = []
                    ver_todos_td = i.find_all("td")
                    cep.append(ver_todos_td[0].a.text)
                    cep.append(ver_todos_td[1].text)
                    cep.append(ver_todos_td[2].text)
                    cep.append(ver_todos_td[3].a.get('title'))
                    cep.append(ver_todos_td[4].text)
                    print(cep)
                    lista_CEP.append(cep)
            
            else:
                cep.append(lista_td[0].a.text)
                cep.append(lista_td[1].a.text)
                cep.append(lista_td[2].text)
                cep.append(lista_td[3].text)
                cep.append(lista_td[4].text)
                print(cep)
                lista_CEP.append(cep)
    except:
        print('Erro, 5 min para retomada')
        time.sleep(120)
        print('Erro, 3 min para retomada')
        time.sleep(60)
        print('Erro, 2 min para retomada')
        time.sleep(60)
        print('Erro, 1 min para retomada')
        time.sleep(60)



df = pd.DataFrame(lista_CEP,columns=['Cep','Rua','Complemento','Bairro','Cidade'])
df.to_csv('Ceps.csv',index=False)    
    
        