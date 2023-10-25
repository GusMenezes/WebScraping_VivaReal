import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures
import pandas as pd


df = pd.read_csv('Exel_and_Csv_Files\\Viva_Real_Scrap.csv',sep=',')

df.to_excel(r'Exel_and_Csv_Files\\Viva_real_Scrap.xlsx')


