import requests
from bs4 import BeautifulSoup
import time ,re, math
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


payload = {}
headers = {
  'X-Domain': 'www.vivareal.com.br',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
  'Cookie': '__cf_bm=ZgTGt6dmIeUY3LfC06kjtCrkJWvoasCS6KiPxWRuEhM-1699977501-0-AZ/aH0E3BRiOu6aTEWqQs/zNcSUuCoCqJBpe5TdOApY1Yd/xQzMOfDSY4KfQBb9o5ygzaUOnO1X4IqmfOVw+76Y=; __cfruid=bd7cd5a4a2129926c45f4d8e9e1524c9723cf8c9-1699977501'
}


url = f"https://glue-api.vivareal.com/v2/listings?addressCity=Uberlândia&addressLocationId=BR>Minas Gerais>NULL>Uberlandia&addressNeighborhood=&addressState=Minas Gerais&addressCountry=Brasil&addressStreet=&addressZone=&addressPointLat=-18.912775&addressPointLon=-48.275523&business=SALE&facets=amenities&unitTypes=HOME&unitSubTypes=CONDOMINIUM&unitTypesV3=CONDOMINIUM&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier,phones),developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,tier),medias,accountLink,link)),totalCount))&size=36&from=0&q=&developmentsSize=5&__vt=mtc:nodecay,B&levels=CITY,UNIT_TYPE&ref=&pointRadius=&isPOIQuery="
resposta = requests.get(url,headers=headers,data=payload,timeout=1)
json = resposta.json()
numero_anuncios = json.get('page').get('metaContent').get('description')
temp = re.findall(r'\d+', numero_anuncios)
numero_anuncios = int(''.join(temp))

print(numero_anuncios)