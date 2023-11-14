import requests,time ,re, math
import pandas as pd

payload = {}
headers = {
  'X-Domain': 'www.vivareal.com.br',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'Cookie': '__cf_bm=ZgTGt6dmIeUY3LfC06kjtCrkJWvoasCS6KiPxWRuEhM-1699977501-0-AZ/aH0E3BRiOu6aTEWqQs/zNcSUuCoCqJBpe5TdOApY1Yd/xQzMOfDSY4KfQBb9o5ygzaUOnO1X4IqmfOVw+76Y=; __cfruid=bd7cd5a4a2129926c45f4d8e9e1524c9723cf8c9-1699977501'
}

lista_url = []  #Lista para guardar todos links de cada Imovel

#Pega a quantidades de anuncios no site
url = f"https://glue-api.vivareal.com/v2/listings?addressCity=Uberlândia&addressLocationId=BR>Minas Gerais>NULL>Uberlandia&addressNeighborhood=&addressState=Minas Gerais&addressCountry=Brasil&addressStreet=&addressZone=&addressPointLat=-18.912775&addressPointLon=-48.275523&business=SALE&facets=amenities&unitTypes=HOME&unitSubTypes=CONDOMINIUM&unitTypesV3=CONDOMINIUM&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier,phones),developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount))&size=36&from=0&q=&developmentsSize=5&__vt=mtc:nodecay,B&levels=CITY,UNIT_TYPE&ref=&pointRadius=&isPOIQuery="
resposta = requests.get(url,headers=headers,data=payload,timeout=1)
json = resposta.json()
numero_anuncios = json.get('page').get('metaContent').get('description')
temp = re.findall(r'\d+', numero_anuncios)
numero_anuncios = int(''.join(temp))


contador = 0
for j in range(0,math.floor(numero_anuncios/36)):
    try:     
        url = f"https://glue-api.vivareal.com/v2/listings?addressCity=Uberlândia&addressLocationId=BR>Minas Gerais>NULL>Uberlandia&addressNeighborhood=&addressState=Minas Gerais&addressCountry=Brasil&addressStreet=&addressZone=&addressPointLat=-18.912775&addressPointLon=-48.275523&business=SALE&facets=amenities&unitTypes=HOME&unitSubTypes=CONDOMINIUM&unitTypesV3=CONDOMINIUM&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier,phones),developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount))&size=36&from={contador}&q=&developmentsSize=5&__vt=mtc:nodecay,B&levels=CITY,UNIT_TYPE&ref=&pointRadius=&isPOIQuery="
        time.sleep(1.5)
        resposta = requests.get(url,headers=headers,data=payload,timeout=1)
        json = resposta.json()
        imoveis = json.get('search').get('result').get('listings')
        print(j)

        for i in imoveis:
            try:
                url_anuncio = i.get('link').get('href')
                url_anuncio = "https://www.vivareal.com.br" + url_anuncio
                lista_url.append(url_anuncio)

            except:
                pass
        contador +=36 

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


df = pd.DataFrame(lista_url,columns=['Url_imovel'])
df.to_csv(r"D:\ginga\Documents\Gustavo\WebScraping_VivaReal\WebScraping_VivaReal\Exel_and_Csv_Files\LISTA_URLS_VIVAREAL.csv",index=False)