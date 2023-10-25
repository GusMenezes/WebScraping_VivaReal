import requests
import time ,re
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json



df = pd.read_csv("D:\\ginga\\Documents\\Gustavo\\WebScraping_VivaReal\\WebScraping_VivaReal\\Exel_and_Csv_Files\\WebScrap_VivaReal1.csv",sep=',')

df = df.drop_duplicates()

df.to_csv('Exel_and_Csv_Files\\WebScrap_VivaReal2.csv',index=False)