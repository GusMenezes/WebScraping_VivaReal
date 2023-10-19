import requests
import time ,re
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

df = pd.read_csv("WebScrap_VivaReal1.csv",sep=',')


lista_url = df['Url_imovel'].copy()

lista_imoveis = []


for i in range(len(lista_url)):
    try:        
        #Request site imovel
        resposta = requests.get(lista_url[i],headers=headers)

        soup = fromstring(resposta.text)

        script = soup.xpath('/html/body/script[1]/text()')

        script = str(script[0])

        js = script.split('/* Other data */\n      ...')
        js = js[1].split('\n    };\n\n  function getSettings()')
        js = js[0]

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
        print(json_object.get('listing').get('suites') )
        if len(json_object.get('listing').get('suites'))==1:
            suites = json_object.get('listing').get('suites')[0]
        else:
            suites = ''
        if len(json_object.get('listing').get('parkingSpaces'))==1:
            parkingSpaces = json_object.get('listing').get('parkingSpaces')[0]
        else:
            parkingSpaces = ''
        status = json_object.get('listing').get('status')
        amenties = json_object.get('listing').get('amanties')
        description = json_object.get('listing').get('description')
        createdAt = json_object.get('listing').get('createdAt')
        floors = json_object.get('listing').get('floors')
        advertiserName = json_object.get('account').get('name')
        advertiserLicenseNumber = json_object.get('account').get('licenseNumber')
        advertiserPhonePrimary = json_object.get('account').get('phone').get('primary')
        advertiserPhoneMobile = json_object.get('account').get('phone').get('mobile')
        urlImovel = lista_url[i]

        data = {
            'ID_VivaReal':id,
            'UnitType':unitType,
            'ListingType':listingType,
            'State':state,
            'City':city,
            'Neighborhood':neighborhood,
            'Street':street,
            'StreetNumber':streetNumber,
            'ZipCode':zipcode,
            'Title':title,
            'ExternalId':externalId,
            'Price':price,
            'Iptu':iptu,
            'CondominiumFee':condominiumFee,
            'UsableAreas':usableAreas,
            'Bedrooms':bedrooms,
            'Bathrooms':bathrooms,
            'Suites':suites,
            'ParkingSpaces':parkingSpaces,
            'Status':status,
            'Amenties':amenties,
            'Description':description,
            'CreatedAt':createdAt,
            'Floors':floors,
            'Advertiser_Name':advertiserName,
            'Advertiser_License':advertiserLicenseNumber,
            'Advertiser_Phone_Primary':advertiserPhonePrimary,
            'Advertiser_Phone_Mobile':advertiserPhoneMobile,
            'Url_Place':urlImovel
        }
        
        lista_imoveis.append(data)
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


df = pd.DataFrame(lista_imoveis)
try:
    df.drop_duplicates()
except:
    j= 1

df.to_csv('Exel_and_Csv_Files\\teste.csv',index=False)
df.to_excel(r'Exel_and_Csv_Files\\Viva_real_Scrap.xlsx')