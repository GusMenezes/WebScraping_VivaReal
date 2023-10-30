import requests
import time ,re
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json

#Headers usado para request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

#Leitura do Csv de Urls de Imoveis e Leitura ou criação de DataFrame de Info de Imoveis
df = pd.read_csv("Exel_and_Csv_Files\LISTA_URLS_VIVAREAL 26-10-2023.csv",sep=',')
try:
    df_imoveis = pd.read_csv("D:\\ginga\\Documents\\Gustavo\\WebScraping_VivaReal\\WebScraping_VivaReal\\Exel_and_Csv_Files\\Viva_Real_Scrap.csv",sep=',')
except:
    df_imoveis = pd.DataFrame(columns=['ID_VivaReal','UnitType','ListingType','State','City','Neighborhood','Street','StreetNumber','ZipCode','Title','ExternalId','Price','Iptu','CondominiumFee','UsableAreas','Bedrooms','Bathrooms','Suites','ParkingSpaces','Status','Amenities','Description','CreatedAt','Floors','Advertiser_Name','Advertiser_License','Advertiser_Phone_Primary','Advertiser_Phone_Mobile','Url_Place'])


#listas que serão usadas no for
lista_url = df['Url_imovel'].copy()
lista_imoveis = []

#session
s = requests.Session()



print(len(lista_url))
pos = len(df_imoveis) #Ultimo imovel guardado 
print(pos)
for pos in range(pos,len(lista_url)):#Para cada url na lista_url
    try:        
        
        #Request site imovel
        time.sleep(1)
        resposta = s.get(lista_url[pos],headers=headers)
        print('Status_Code=',resposta.status_code)
        
        #Obtendo script desejado
        soup = fromstring(resposta.text)
        script = soup.xpath('/html/body/script[1]/text()')

        #Tratamento do script para que possa ser trabalhado 
        script = str(script[0])
        js = script.split('/* Other data */\n      ...')
        js = js[1].split('\n    };\n\n  function getSettings()')
        js = js[0]

        
        #Transformando script tipo string para tipo dicionario
        json_object = json.loads(js.strip("()"))

        #Obtendo infos desejadas do script
        try: #Pega Id do proprio viva real
            id = json_object.get('listing').get('id')
        except:
            id = ''
        
        try: #Pega tipo de unidade do imovel
            unitType = json_object.get('listing').get('unitTypes')[0]
        except:
            unitType = ''
        
        try: #Condiçao do Imovel
            listingType = json_object.get('listing').get('listingType')
        except:
            listingType = ''

        try: #Estado
            state = json_object.get('listing').get('address').get('state')
        except:
            state = ''

        try: #Cidade
            city = json_object.get('listing').get('address').get('city')
        except:
            city = ''

        try: #bairro
            neighborhood = json_object.get('listing').get('address').get('neighborhood')
        except:
            neighborhood = ''
        
        try: #Rua
            street = json_object.get('listing').get('address').get('street')
        except:
            street = ''
        
        try: #Numero do imovel
            streetNumber = json_object.get('listing').get('address').get('streetNumber')
        except:
            streetNumber = ''

        try: #Cep
            zipcode = json_object.get('listing').get('address').get('zipCode')
        except:''

        try: #Titulo do anuncio
            title = json_object.get('listing').get('title')
        except:
            title = ''

        try: #Id da imobiliaria
            externalId = json_object.get('listing').get('externalId')
        except:
            externalId = ''

        try: #Preco imovel
            price = json_object.get('listing').get('pricingInfos')[0].get('price')
        except:
            price = ''

        try: #iptu do imovel
            iptu = json_object.get('listing').get('pricingInfos')[0].get('yearlyIptu')
        except:
            iptu = ''
        
        try: #Preço do Condominio do imovel
            condominiumFee = json_object.get('listing').get('pricingInfos')[0].get('monthlyCondoFee')
        except:
            condominiumFee = ''
        
        try: #Area do imovel
            usableAreas = json_object.get('listing').get('usableAreas')[0]
        except:
            usableAreas = ''
        
        try: #Numero de quartos 
            bedrooms = json_object.get('listing').get('bedrooms')[0]
        except:
            bedrooms = ''

        try: #Numero de banheiros 
            bathrooms = json_object.get('listing').get('bathrooms')[0]
        except:
            bathrooms = ''

        try: #Numero de suites
            suites = json_object.get('listing').get('suites')[0]
        except:
            suites = ''

        try: #Numero de espaços de garagem
            parkingSpaces = json_object.get('listing').get('parkingSpaces')[0]
        except:
            parkingSpaces = ''
        
        try: #Status do anuncio
            status = json_object.get('listing').get('status')
        except:
            status = ''

        try: #Caracteristicas do imovel
            amenities = json_object.get('listing').get('amenities')
        except:
            amenities = ''

        try: #Descricao do imovel
            description = json_object.get('listing').get('description').replace('<br>','')
        except:
            description = ''

        try: #data de criaçao do anuncio
            createdAt = json_object.get('listing').get('createdAt')
        except:
            createdAt = ''
        
        try: #Andares
            floors = json_object.get('listing').get('floors')
        except:
            floors = ''
        
        try: #Nome do Anunciante 
            advertiserName = json_object.get('account').get('name')
        except:
            advertiserName = ''
        
        try: #Numero de Licença do anunciante
            advertiserLicenseNumber = json_object.get('account').get('licenseNumber')
        except:
            advertiserLicenseNumber = ''
        
        try: #telefone primario do anunciante
            advertiserPhonePrimary = json_object.get('account').get('phone').get('primary')
        except:
            advertiserPhonePrimary = ''
        
        try: #telefone secundario do anunciante
            advertiserPhoneMobile = json_object.get('account').get('phone').get('mobile')
        except:
            advertiserPhoneMobile = ''
        
        #Url do anuncio do imovel
        urlImovel = lista_url[pos]

        #Dicionario para guardar todas as variaveis
        data = {
            'ID_VivaReal':id,                                   #ID VivaReal
            'UnitType':unitType,                                #Tipo de Imovel
            'ListingType':listingType,                          #Condiçao do Imovel
            'State':state,                                      #Estado
            'City':city,                                        #Cidade
            'Neighborhood':neighborhood,                        #Bairro
            'Street':street,                                    #Rua
            'StreetNumber':streetNumber,                        #Numero na Rua
            'ZipCode':int(zipcode),                             #Cep
            'Title':title,                                      #Titulo do Anuncio
            'ExternalId':externalId,                            #Id da Imobiliaria
            'Price':float(price),                               #Preço do Imovel
            'Iptu':iptu,                                        #Iptu
            'CondominiumFee':condominiumFee,                    #Preço do Condominio
            'UsableAreas':usableAreas,                          #Area do imovel
            'Bedrooms':bedrooms,                                #Numero de quartos
            'Bathrooms':bathrooms,                              #  --   de banheiros
            'Suites':suites,                                    #  --   de Suites
            'ParkingSpaces':parkingSpaces,                      #  --   de Vagas de Garagem
            'Status':status,                                    #Status do Anuncio (Ativado/Desativado)
            'Amenities':amenities,                              #Caracteristicas do Imovel
            'Description':description,                          #Descriçao do Imovel
            'CreatedAt':createdAt,                              #Data de Criaçao do Imovel
            'Floors':floors,                                    #Numero de Andares
            'Advertiser_Name':advertiserName,                   #Nome do Anunciante
            'Advertiser_License':advertiserLicenseNumber,       #Numero de licença do Anunciante
            'Advertiser_Phone_Primary': advertiserPhonePrimary, #Telefone Primario do Anunciante
            'Advertiser_Phone_Mobile': advertiserPhoneMobile,   #Telefone Secundario do Anunciante
            'Url_Place':urlImovel                               #Url do Anuncio 
        }
        
        #Guarda todas as Infos do Imoveis em uma Lista
        lista_imoveis.append(data)
        print('Posição =',pos) #print para acompanhamento do script


    #Tratamento de erro: Caso aconteça algum empecilho na obtençao dos dados do imovel, para o Script por 5min e tenta de novo
    except Exception as e:
        print(e)
        print('Erro, 5 min para retomada')
        time.sleep(120)
        print('Erro, 3 min para retomada')
        time.sleep(60)
        print('Erro, 2 min para retomada')
        time.sleep(60)
        print('Erro, 1 min para retomada')
        time.sleep(60)

    #Para cada Imovel, Atualiza arquivo Csv
    df_imoveis = pd.concat([df_imoveis,pd.DataFrame(lista_imoveis)],ignore_index=True)
    df_imoveis.to_csv("D:\\ginga\\Documents\\Gustavo\\WebScraping_VivaReal\\WebScraping_VivaReal\\Exel_and_Csv_Files\\Viva_Real_Scrap.csv",index=False)
    #Zera a lista para não dar erro
    lista_imoveis = []


#Cria data Frame
df = pd.DataFrame(lista_imoveis)
#try:
#    df.drop_duplicates()
#except:
#    j= 1

df.to_excel(r"D:\\ginga\Documents\\Gustavo\WebScraping_VivaReal\\WebScraping_VivaReal\\Exel_and_Csv_Files\\Viva_Real_Scrap.xlsx")