import requests


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
r = requests.get('https://resizedimgs.zapimoveis.com.br/fit-in/800x360/named.images.sp/fd3946db6ffab76905cda06001e40658/apartamento-com-3-quartos-a-venda-185m-no-altamira-uberlandia.jpg',headers=headers)

with open('foto1.jpg','wb') as f:
    f.write(r.content)