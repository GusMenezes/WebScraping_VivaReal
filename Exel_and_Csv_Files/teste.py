import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time ,re
import pandas as pd


list_links = []

with open("proxy_list.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        list_links.append(p)

df = pd.DataFrame(columns=['links'])
for i in list_links:
    df.loc[len(df.index)] = i


df.to_csv('teste.csv',index=False)