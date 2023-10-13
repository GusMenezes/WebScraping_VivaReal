import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures


proxylist = []

with open("proxy_list.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        proxylist.append(p)
     

# URL de teste para verificar se o proxy está funcionando
test_url = "https://www.vivareal.com.br/imovel/apartamento-2-quartos-grand-ville-bairros-uberlandia-com-garagem-55m2-aluguel-RS1600-id-2661565901/"

# Lista de proxies a serem testados

for proxy in proxylist:
    try:
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(proxy)
    except:
        continue
