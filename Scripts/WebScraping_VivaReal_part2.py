import requests
import time ,re
import datetime
import mysql.connector
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json


#tempo em que o script python foi iniciado
tempo = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

#Estabelecendo conexao com sgbd
conexao = mysql.connector.connect(
    host = '193.203.183.54',
    user = 'perdigueiro',
    password = 'V3nc3d0r3s@23',
    database = 'perdigueiro',
)
cursor = conexao.cursor()


#Headers usado para request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

#Leitura do Csv de Urls de Imoveis e Leitura ou criação de DataFrame de Info de Imoveis
df = pd.read_csv("Exel_and_Csv_Files\LISTA_URLS_VIVAREAL 26-10-2023.csv",sep=',')

#listas que serão usadas no for
lista_url = df['Url_imovel'].copy()
lista_imoveis = []

#session
s = requests.Session()



print(len(lista_url))


for pos in range(0,len(lista_url)):#Para cada url na lista_url
    try:        
        
        #Request site imovel
        time.sleep(1)
        resposta = s.get(lista_url[pos],headers=headers)
        print('Status_Code=',resposta.status_code)
        
        #HTML para pegar informacoes especificas
        html = BeautifulSoup(resposta.text,'html.parser')


        #Obtendo script desejado
        soup = fromstring(resposta.text)
        script = soup.xpath('/html/body/script[1]/text()')

        #Tratamento do script para que possa ser trabalhado 
        script = str(script[0])
        js = script.split('/* Other data */\n      ...')
        js = js[1].split('\n    };\n\n  function getSettings()')
        js = js[0]

        
        #Transformando script tipo string para tipo dicionario
        json_object = json.loads(js.strip("()"))

        #Obtendo infos desejadas do script
        try: #Pega Id do proprio viva real
            id_ambiente = json_object.get('listing').get('id')
            id_ambiente = int(id_ambiente)/1000
        except:
            id_ambiente = ''
        
        try: #Pega tipo de unidade do imovel
            tipo_imovel = json_object.get('listing').get('unitTypes')[0]
        except:
            tipo_imovel = ''
        
        try: #Condiçao do Imovel
            condicao_imovel = json_object.get('listing').get('listingType')
        except:
            condicao_imovel = ''

        try: #Estado
            estado = json_object.get('listing').get('address').get('state')
        except:
            estado = ''

        try: #Cidade
            cidade = json_object.get('listing').get('address').get('city')
        except:
            cidade = ''

        try: #bairro
            bairro = json_object.get('listing').get('address').get('neighborhood')
        except:
            bairro = ''
        
        try: #Rua
            rua = json_object.get('listing').get('address').get('street')
        except:
            rua = ''
        
        try: #Numero do imovel
            numero_casa = json_object.get('listing').get('address').get('streetNumber')
        except:
            numero_casa = ''

        try: #Cep
            cep = json_object.get('listing').get('address').get('zipCode')
        except:
            cep = ''

        try: #Titulo do anuncio
            titulo = json_object.get('listing').get('title')
        except:
            titulo = ''

        try: #Id da imobiliaria
            codigo_imobiliaria = json_object.get('listing').get('externalId')
        except:
            codigo_imobiliaria = ''

        try: #Preco imovel
            preco = json_object.get('listing').get('pricingInfos')[0].get('price')
        except:
            preco = ''

        try: #iptu do imovel
            iptu = json_object.get('listing').get('pricingInfos')[0].get('yearlyIptu')
        except:
            iptu = ''
        
        try: #Preço do Condominio do imovel
            preco_condominio = json_object.get('listing').get('pricingInfos')[0].get('monthlyCondoFee')
        except:
            preco_condominio = ''
        
        try: #Area do imovel
            area = json_object.get('listing').get('usableAreas')[0]
        except:
            area = ''
        
        try: #Numero de quartos 
            quartos = json_object.get('listing').get('bedrooms')[0]
        except:
            quartos = ''

        try: #Numero de banheiros 
            banheiros = json_object.get('listing').get('bathrooms')[0]
        except:
            banheiros = ''

        try: #Numero de suites
            suites = json_object.get('listing').get('suites')[0]
        except:
            suites = ''

        try: #Numero de espaços de garagem
            garagens = json_object.get('listing').get('parkingSpaces')[0]
        except:
            garagens = ''
        
        try: #Status do anuncio
            status_anuncio = json_object.get('listing').get('status')
        except:
            status_anuncio = ''

        try: #Caracteristicas do imovel
            caracteristicas = []
            ul_caracteristicas = html.find('ul',class_='amenities__list')
            li_caracteristicas = ul_caracteristicas.find_all('li')
            for li in li_caracteristicas:
                caracteristicas.append(li.text.strip())
        except:
            amenities = ''

        try: #Descricao do imovel
            descricao = json_object.get('listing').get('description').replace('<br>','').replace('"','*').replace("'",'*')
        except:
            descricao = ''

        try: #data de criaçao do anuncio
            data_criacao = json_object.get('listing').get('createdAt')
        except:
            data_criacao = ''
        
        try: #Nome do Anunciante 
            anunciante = json_object.get('account').get('name')
        except:
            anunciante = ''
        
        try: #Numero de Licença do anunciante
            licenca_anunciante = json_object.get('account').get('licenseNumber')
        except:
            licenca_anunciante = ''
        
        try: #telefone primario do anunciante
            telefone_primario_anunciante = json_object.get('account').get('phone').get('primary')
        except:
            telefone_primario_anunciante = ''
        
        try: #telefone secundario do anunciante
            telefone_secundario_anunciante = json_object.get('account').get('phone').get('mobile')
        except:
            telefone_secundario_anunciante = ''
        
        #Url do anuncio do imovel
        urlImovel = lista_url[pos]

        #Dicionario para guardar todas as variaveis
        data = {
            'id_ambiente':id_ambiente,                                          #ID VivaReal
            'tipo_imovel':tipo_imovel,                                          #Tipo de Imovel
            'condicao_imovel':condicao_imovel,                                  #Condiçao do Imovel
            'estado':estado,                                                    #Estado
            'cidade':cidade,                                                    #Cidade
            'bairro':bairro,                                                    #Bairro
            'rua':rua,                                                          #Rua
            'numero_casa':numero_casa,                                          #Numero na Rua
            'cep':int(cep),                                                     #Cep
            'titulo':titulo,                                                    #Titulo do Anuncio
            'codigo_imobiliaria':codigo_imobiliaria,                            #Id da Imobiliaria
            'preco':float(preco),                                               #Preço do Imovel
            'iptu':iptu,                                                        #Iptu
            'preco_condominio':preco_condominio,                                #Preço do Condominio
            'area':area,                                                        #Area do imovel
            'quartos':quartos,                                                  #Numero de quartos
            'banheiros':banheiros,                                              #  --   de banheiros
            'suites':suites,                                                    #  --   de Suites
            'garagens':garagens,                                                #  --   de Vagas de Garagem
            'status_anuncio':status_anuncio,                                    #Status do Anuncio (Ativado/Desativado)
            'caracteristicas':caracteristicas,                                  #Caracteristicas do Imovel
            'descricao':descricao,                                              #Descriçao do Imovel
            'data_criacao':data_criacao,                                        #Data de Criaçao do Imovel
            'anunciante':anunciante,                                            #Nome do Anunciante
            'licenca_anunciante':licenca_anunciante,                            #Numero de licença do Anunciante
            'telefone_primario_anunciante': telefone_primario_anunciante,       #Telefone Primario do Anunciante
            'telefone_secundario_anunciante': telefone_secundario_anunciante,   #Telefone Secundario do Anunciante
            'url':urlImovel                                                     #Url do Anuncio 
        }
        
        #Guarda as infos dos imoveis na tabela garimpo do banco de dados, e pega o id_garimpo gerado
        comando = f"""INSERT INTO garimpo (idambiente, ambiente, caminho , criadopor, criadoem, alteradopor, alteradoem) 
                        VALUES ("{id_ambiente}","VivaReal", "{urlImovel}", "Gustavo", "{tempo}", "Gustavo", "{tempo}")"""
        cursor.execute(comando)
        conexao.commit()
        comando = """ SELECT LAST_INSERT_ID();"""
        cursor.execute(comando)
        id_garimpo = cursor.fetchall()
        id_garimpo = id_garimpo[0][0]
        

        tempo = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        #Guarda as infos na tabela garimpo dados
        for item in data.items():
            if isinstance(item[1],list):
                for c in item[1]:
                    comando = f"""INSERT INTO garimpodados (idgarimpo , chave, valor , criadopor, criadoem, alteradopor, alteradoem) 
                                VALUES ("{id_garimpo}","{item[0]}", "{c}", "Gustavo", "{tempo}", "Gustavo", "{tempo}")"""
                    cursor.execute(comando)
                    conexao.commit()
            else:
                comando = f"""INSERT INTO garimpodados (idgarimpo , chave, valor , criadopor, criadoem, alteradopor, alteradoem) 
                                VALUES ("{id_garimpo}","{item[0]}", "{item[1]}", "Gustavo", "{tempo}", "Gustavo", "{tempo}")"""
                cursor.execute(comando)
                conexao.commit()

        print('Posição =',pos) #print para acompanhamento do script


    #Tratamento de erro: Caso aconteça algum empecilho na obtençao dos dados do imovel, para o Script por 5min e tenta de novo
    except Exception as e:
        print(e)
        print('Erro, 5 min para retomada')
        time.sleep(120)
        print('Erro, 3 min para retomada')
        time.sleep(60)
        print('Erro, 2 min para retomada')
        time.sleep(60)
        print('Erro, 1 min para retomada')
        time.sleep(60)

    

#fechando conexao com banco de dados
cursor.close()
conexao.close()

