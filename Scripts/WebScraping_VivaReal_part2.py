import requests
import time ,re
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

df = pd.read_csv("D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\WebScrap_VivaReal1.csv",sep=',')
try:
    df_imoveis = pd.read_csv('D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Exel_and_Csv_Files\Viva_Real_Scrap.csv',sep=',')
except:
    df_imoveis = pd.DataFrame(columns=['ID_VivaReal','UnitType','ListingType','State','City','Neighborhood','Street','StreetNumber','ZipCode','Title','ExternalId','Price','Iptu','CondominiumFee','UsableAreas','Bedrooms','Bathrooms','Suites','ParkingSpaces','Status','Amenities','Description','CreatedAt','Floors','Advertiser_Name','Advertiser_License','Advertiser_Phone_Primary','Advertiser_Phone_Mobile','Url_Place'])

lista_url = df['Url_imovel'].copy()

lista_imoveis = []

pos = int(input('Posição inicial:  '))
cont = 0
for pos in range(pos,len(lista_url)):
    try:        
        #Request site imovel
        time.sleep(2)
        resposta = requests.get(lista_url[pos],headers=headers)
        print(resposta.status_code)

        soup = fromstring(resposta.text)

        script = soup.xpath('/html/body/script[1]/text()')

        script = str(script[0])

        js = script.split('/* Other data */\n      ...')
        js = js[1].split('\n    };\n\n  function getSettings()')
        js = js[0]

        with open('teste.txt','w')as a:
            a.write(js.strip("()"))

        json_object = json.loads(js.strip("()"))

        id = json_object.get('listing').get('id')
        unitType = json_object.get('listing').get('unitTypes')[0]
        listingType = json_object.get('listing').get('listingType')
        state = json_object.get('listing').get('address').get('state')
        city = json_object.get('listing').get('address').get('city')
        neighborhood = json_object.get('listing').get('address').get('neighborhood')    
        street = json_object.get('listing').get('address').get('street')
        streetNumber = json_object.get('listing').get('address').get('streetNumber')
        zipcode = json_object.get('listing').get('address').get('zipCode')
        title = json_object.get('listing').get('title')
        externalId = json_object.get('listing').get('externalId')
        price = json_object.get('listing').get('pricingInfos')[0].get('price')
        iptu = json_object.get('listing').get('pricingInfos')[0].get('yearlyIptu')
        condominiumFee = json_object.get('listing').get('pricingInfos')[0].get('monthlyCondoFee')
        usableAreas = json_object.get('listing').get('usableAreas')[0]
        bedrooms = json_object.get('listing').get('bedrooms')[0]
        bathrooms = json_object.get('listing').get('bathrooms')[0]
        if len(json_object.get('listing').get('suites'))==1:
            suites = json_object.get('listing').get('suites')[0]
        else:
            suites = ''
        if len(json_object.get('listing').get('parkingSpaces'))==1:
            parkingSpaces = json_object.get('listing').get('parkingSpaces')[0]
        else:
            parkingSpaces = ''
        status = json_object.get('listing').get('status')
        amenities = json_object.get('listing').get('amenities')
        description = json_object.get('listing').get('description')
        createdAt = json_object.get('listing').get('createdAt')
        floors = json_object.get('listing').get('floors')
        advertiserName = json_object.get('account').get('name')
        advertiserLicenseNumber = json_object.get('account').get('licenseNumber')
        advertiserPhonePrimary = json_object.get('account').get('phone').get('primary')
        advertiserPhoneMobile = json_object.get('account').get('phone').get('mobile')
        urlImovel = lista_url[pos]

        data = {
            'ID_VivaReal':id,
            'UnitType':unitType,
            'ListingType':listingType,
            'State':state,
            'City':city,
            'Neighborhood':neighborhood,
            'Street':street,
            'StreetNumber':streetNumber,
            'ZipCode':int(zipcode),
            'Title':title,
            'ExternalId':externalId,
            'Price':float(price),
            'Iptu':iptu,
            'CondominiumFee':condominiumFee,
            'UsableAreas':usableAreas,
            'Bedrooms':bedrooms,
            'Bathrooms':bathrooms,
            'Suites':suites,
            'ParkingSpaces':parkingSpaces,
            'Status':status,
            'Amenities':amenities,
            'Description':description,
            'CreatedAt':createdAt,
            'Floors':floors,
            'Advertiser_Name':advertiserName,
            'Advertiser_License':advertiserLicenseNumber,
            'Advertiser_Phone_Primary': advertiserPhonePrimary,
            'Advertiser_Phone_Mobile': advertiserPhoneMobile,
            'Url_Place':urlImovel
        }
        
        lista_imoveis.append(data)
        print(pos)
        cont +=1


    except:
        print('Erro, 5 min para retomada')
        time.sleep(120)
        print('Erro, 3 min para retomada')
        time.sleep(60)
        print('Erro, 2 min para retomada')
        time.sleep(60)
        print('Erro, 1 min para retomada')
        time.sleep(60)

    df_imoveis = pd.concat([df_imoveis,pd.DataFrame(lista_imoveis)],ignore_index=True)
    df_imoveis.to_csv('D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Exel_and_Csv_Files\Viva_Real_Scrap.csv',index=False)
    lista_imoveis = []


df = pd.DataFrame(lista_imoveis)
#try:
#    df.drop_duplicates()
#except:
#    j= 1

df.to_excel(r'Exel_and_Csv_Files\\Viva_real_Scrap.xlsx')