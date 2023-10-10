import threading
import queue

import requests

q = queue.Queue()
valid_proxys = []

with open("proxy_list.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)



def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("https://www.vivareal.com.br/imovel/apartamento-3-quartos-santa-maria-bairros-uberlandia-com-garagem-108m2-venda-RS650000-id-2660442378/",
                               proxies={"http":proxy,
                                        "https":proxy})
        
        except:
            continue

        if res.status_code == 200:
            print(proxy)


for _ in range(10):
    threading.Thread(target=check_proxies).start()