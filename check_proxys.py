import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures


proxylist = []

with open("proxy_list.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        proxylist.append(p)
     


def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get('https://www.vivareal.com.br/', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
        print('r.json(), r.status_code')
    except requests.ConnectionError as err:
        print('.')
    return proxy



#check them all with futures super quick
with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxylist)



