import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
resposta = requests.get('https://www.vivareal.com.br/imovel/apartamento-2-quartos-tubalina-bairros-uberlandia-com-garagem-68m2-venda-RS480000-id-2660981065/',headers=headers)


soup = fromstring(resposta.content)

script = soup.xpath('/html/body/script[1]/text()')

script = str(script[0])

js = script.split('/* Other data */\n      ...')
js = js[1].split('\n    };\n\n  function getSettings()')
js = js[0]

json_object = json.loads(js.strip("()"))


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_object, f, ensure_ascii=False, indent=5)