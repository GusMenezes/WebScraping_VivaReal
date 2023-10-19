import requests
import time ,re
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json



df = pd.read_csv("WebScrap_VivaReal1.csv",sep=',')

df.drop_duplicates()

df.to_csv('WebScrap_VivaReal.csv',index=False)