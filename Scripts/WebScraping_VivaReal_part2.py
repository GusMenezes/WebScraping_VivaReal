import requests
import time
import datetime
import mysql.connector
import pandas as pd
from bs4 import BeautifulSoup
from lxml.html import fromstring
import json
import numpy as np
from pathlib import Path


def traduz_palavra(palavra):
    dicionario_traducoes = {
        "USED": "usado",
        "DEVELOPMENT": "desenvolvimento",
        "APARTMENT": "apartamento",
        "HOME": "casa",
        "CONDOMINIUM": "condominio",
        "ADMINISTRATION": "administracao",
        "ADULT_GAME_ROOM": "salao_de_jogos",
        "ADULT_POOL": "piscina_para_adultos",
        "AIR_CONDITIONING": "ar_condicionado",
        "ALARM_SYSTEM": "sistema_de_alarme",
        "ALUMINUM_WINDOW": "janela_de_aluminio",
        "AMERICAN_KITCHEN": "cozinha_americana",
        "ARMORED_SECURITY_CABIN": "cabine_de_seguranca_blindada",
        "ARTESIAN_WELL": "poco_artesiano",
        "BACKYARD": "quintal",
        "BALCONY": "sacada",
        "BAR": "bar",
        "BARBECUE_BALCONY": "sacada_com_churrasqueira",
        "BARBECUE_GRILL": "churrasqueira",
        "BATHROOM_CABINETS": "armarios_de_banheiro",
        "BATHTUB": "banheira",
        "BEAUTY_CENTER": "centro_de_beleza",
        "BEDROOM_WARDROBE": "guarda-roupa_de_quarto",
        "BICYCLES_PLACE": "bicicletario",
        "BLINDEX_BOX": "box_de_blindex",
        "BUILTIN_WARDROBE": "guarda-roupa_embutido",
        "BURNT_CEMENT": "cimento_queimado",
        "CABLE_TV": "tv_a_cabo",
        "CARETAKER": "zelador",
        "CARETAKER_HOUSE": "casa_do_zelador",
        "CHILDRENS_POOL": "piscina_infantil",
        "CINEMA": "cinema",
        "CLOSET": "closet",
        "COLD_FLOOR": "piso_frio",
        "CONCIERGE_24H": "portaria_24_horas",
        "COOKER": "fogao",
        "COPA": "copa",
        "CORNER_PROPERTY": "propriedade_de_esquina",
        "COVENTION_HALL": "salao_de_festas",
        "COVERAGE": "cobertura",
        "COVERED_POOL": "piscina_coberta",
        "COWORKING": "coworking",
        "DECK": "deck",
        "DEPOSIT": "deposito",
        "DIGITAL_LOCKER":"cadeado_digital",
        "DINNER_ROOM": "sala_de_jantar",
        "DISABLED_ACCESS": "acesso_para_deficientes",
        "ECO_CONDOMINIUM": "condominio_ecologico",
        "ECO_GARBAGE_COLLECTOR": "coletor_de_lixo",
        "EDICULE": "edícula",
        "ELECTRIC_GENERATOR": "gerador_eletrico",
        "ELECTRONIC_GATE": "portao_eletronico",
        "ELETRIC_CHARGER": "carregador_eletrico",
        "ELEVATOR": "elevador",
        "EMPLOYEE_DEPENDENCY":"quarto_de_servico",
        "ENTRANCE_HALL": "hall_de_entrada",
        "ESSENTIAL_PUBLIC_SERVICES": "servicos_publicos_essenciais",
        "EXTERIOR_VIEW": "vista_exterior",
        "FENCE": "cerca",
        "FIREPLACE": "lareira",
        "FITNESS_ROOM": "sala_de_ginastica",
        "FOOTBALL_FIELD": "campo_de_futebol",
        "FRUIT_TREES": "arvores_frutiferas",
        "FULL_CABLING": "cabeamento_completo",
        "FULL_FLOOR": "piso_inteiro",
        "FURNISHED": "mobiliado",
        "GAMES_ROOM": "sala_de_jogos",
        "GARAGE": "garagem",
        "GARAGE_BAND": "estudio_de_musica",
        "GARDEN": "jardim",
        "GATED_COMMUNITY": "condominio_fechado",
        "GOLF_FIELD": "campo_de_golfe",
        "GOURMET_BALCONY": "sacada_gourmet",
        "GOURMET_KITCHEN": "cozinha_gourmet",
        "GOURMET_SPACE": "espaco_gourmet",
        "GRASS": "grama",
        "GRAVEL": "cascalho",
        "GREEN_SPACE": "espaco_verde",
        "GUEST_PARKING": "estacionamento_para_visitantes",
        "GYM": "academia",
        "HEATED_POOL": "piscina_aquecida",
        "HEATING": "aquecimento",
        "HIGH_CEILING_HEIGHT": "pe_direito_alto",
        "HIKING_TRAIL": "pista_caminhada",
        "HOME_CINEMA": "cinema_em_casa",
        "HOME_OFFICE": "escritorio_em_casa",
        "HOT_TUB": "ofuro",
        "INDOOR_SOCCER": "futebol_de_salao",
        "INTEGRATED_ENVIRONMENTS": "ambientes_integrados",
        "INTERCOM": "interfone",
        "INTERNET_ACCESS": "acesso_a_internet",
        "KITCHEN": "cozinha",
        "KITCHEN_CABINETS": "armarios_de_cozinha",
        "LAKE": "lago",
        "LAKE_VIEW": "vista_para_o_lago",
        "LAMINATED_FLOOR": "piso_laminado",
        "LARGE_KITCHEN": "cozinha_ampla",
        "LARGE_ROOM": "sala_ampla",
        "LARGE_WINDOW": "janela_grande",
        "LAUNDRY": "lavanderia",
        "LAVABO": "lavabo",
        "LIBRARY": "biblioteca",
        "LUNCH_ROOM": "sala_de_jantar",
        "MASSAGE_ROOM": "sala_de_massagem",
        "MEZZANINE": "mezanino",
        "MOUNTAIN_VIEW": "vista_para_a_montanha",
        "NATURAL_VENTILATION": "ventilacao_natural",
        "NEAR_ACCESS_ROADS": "proximo_a_vias_de_acesso",
        "NEAR_HOSPITAL": "proximo_a_hospital",
        "NEAR_PUBLIC_TRANSPORT": "proximo_a_transporte_publico",
        "NEAR_SCHOOL": "proximo_a_escola",
        "NEAR_SHOPPING_CENTER": "proximo_a_centro_comercial",
        "NEAR_SHOPPING_CENTER_2": "proximo_a_centro_comercial_2",
        "NUMBER_OF_FLOORS": "numero_de_andares",
        "ORCHID_PLACE": "espaco_para_orquideas",
        "PANORAMIC_VIEW": "vista_panoramica",
        "PANTRY": "despensa",
        "PARKING": "estacionamento",
        "PARTY_HALL": "salao_de_festas",
        "PATROL": "patrulha",
        "PAVED_STREET": "rua_pavimentada",
        "PET_SPACE": "espaco_para_animais_de_estimacao",
        "PETS_ALLOWED": "animais_de_estimacao_permitidos",
        "PIZZA_OVEN": "forno_de_pizza",
        "PLANNED_FURNITURE": "moveis_planejados",
        "PLAYGROUND": "playground",
        "POMAR": "pomar",
        "POOL": "piscina",
        "POOL_BAR": "bar_na_piscina",
        "PORCELAIN": "porcelanato",
        "PRIVATE_POOL": "piscina_privativa",
        "RECEPTION": "recepcao",
        "RECREATION_AREA": "area_de_lazer",
        "REFLECTING_POOL": "piscina_espelhada",
        "RESTAURANT": "restaurante",
        "REVERSIBLE_ROOM": "sala_reversivel",
        "RIVER": "rio",
        "SAFETY_CIRCUIT": "circuito_de_seguranca",
        "SANCA": "sanca",
        "SAND_PIT": "caixa_de_areia",
        "SAUNA": "sauna",
        "SEA_VIEW": "vista_para_o_mar",
        "SECURITY_24_HOURS": "seguranca 24 horas",
        "SECURITY_CABIN": "cabine_de_seguranca",
        "SECURITY_CAMERA": "camera_de_seguranca",
        "SERVICE_AREA": "area_de_servico",
        "SERVICE_BATHROOM": "banheiro_de_servico",
        "SERVICE_ENTRANCE": "entrada_de_servico",
        "SKATE_LANE": "pista_de_skate",
        "SLAB": "laje",
        "SMART_CONDOMINIUM": "condominio_inteligente",
        "SOLARIUM": "solario",
        "SPA": "spa",
        "SPORTS_COURT": "quadra_de_esportes",
        "SQUARE": "praca",
        "SQUASH": "squash",
        "STAIR": "escada",
        "TEEN_SPACE": "espaco_para_adolescentes",
        "TENNIS_COURT": "quadra_de_tenis",
        "TOYS_PLACE": "espaco_para_brinquedos",
        "TREE_CLIMBING": "escalada_em_arvores",
        "WALL_BALCONY": "sacada_com_muro",
        "WATCHMAN": "vigia",
        "WATER_TANK": "caixa_d'agua",
        "WHIRLPOOL": "hidromassagem",
        "YOUTH_GAME_ROOM": "sala_de_jogos_para_jovens",
        "ZEN_SPACE": "espaco_zen"
    }

    if palavra in dicionario_traducoes:
        return dicionario_traducoes[palavra]
    else:
        return palavra

#Cria Diretorio para Imagens
parent_dir = Path().parent / 'Imagens_Imoveis'
parent_dir.mkdir(exist_ok=True)

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


for pos in range(0,10):#Para cada url na lista_url
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

        try:
            imagens = html.find_all('li',class_='carousel__slide js-carousel-item-wrapper')
        except:
            imagens = None

        #Obtendo infos desejadas do script
        try: #Pega Id do proprio viva real
            id_ambiente = json_object.get('listing').get('id')
        except:
            id_ambiente = None
        
        try: #Pega tipo de unidade do imovel
            tipo_imovel = json_object.get('listing').get('unitTypes')[0]
        except:
            tipo_imovel = None
        
        try: #Condiçao do Imovel
            novo_usado = json_object.get('listing').get('listingType')
        except:
            novo_usado = None

        try: #Estado
            estado = json_object.get('listing').get('address').get('state')
        except:
            estado = None

        try: #Cidade
            cidade = json_object.get('listing').get('address').get('city')
        except:
            cidade = None

        try: #bairro
            bairro = json_object.get('listing').get('address').get('neighborhood')
        except:
            bairro = None
        
        try: #Rua
            rua = json_object.get('listing').get('address').get('street')
        except:
            rua = None
        
        try: #Numero do imovel
            numero = json_object.get('listing').get('address').get('streetNumber')
        except:
            numero = None

        try: #Cep
            cep = json_object.get('listing').get('address').get('zipCode')
        except:
            cep = None

        try: #Titulo do anuncio
            titulo = json_object.get('listing').get('title')
        except:
            titulo = None

        try: #Id da imobiliaria
            cod_anunciante = json_object.get('listing').get('externalId')
        except:
            cod_anunciante = None

        try: #Preco imovel
            preco = json_object.get('listing').get('pricingInfos')[0].get('price')
        except:
            preco = None

        try: #iptu do imovel
            iptu = json_object.get('listing').get('pricingInfos')[0].get('yearlyIptu')
        except:
            iptu = None
        
        try: #Preço do Condominio do imovel
            taxa_condominio = json_object.get('listing').get('pricingInfos')[0].get('monthlyCondoFee')
        except:
            taxa_condominio = None
        
        try: #Area do imovel
            area_privativa = json_object.get('listing').get('usableAreas')[0]
        except:
            area_privativa = None
        
        try: #Numero de quartos 
            quartos = json_object.get('listing').get('bedrooms')[0]
        except:
            quartos = None

        try: #Numero de banheiros 
            banheiros = json_object.get('listing').get('bathrooms')[0]
        except:
            banheiros = None

        try: #Numero de suites
            suites = json_object.get('listing').get('suites')[0]
        except:
            suites = None

        try: #Numero de espaços de garagem
            garagens = json_object.get('listing').get('parkingSpaces')[0]
        except:
            garagens = None
        
        try: #Status do anuncio
            status = json_object.get('listing').get('status')
        except:
            status = None

        try: #Caracteristicas do imovel
            caracteristicas =  json_object.get('listing').get('amenities')
        except:
            caracteristicas = None

        try: #Descricao do imovel
            descricao = json_object.get('listing').get('description').replace('<br>','').replace('"','*').replace("'",'*')
        except:
            descricao = None

        try: #data de criaçao do anuncio
            data_anuncio = json_object.get('listing').get('createdAt')
        except:
            data_anuncio = None
        
        try: #Nome do Anunciante 
            nome_anunciante = json_object.get('account').get('name')
        except:
            nome_anunciante = None
        
        try: #Numero de Licença do anunciante
            creci = json_object.get('account').get('licenseNumber')
        except:
            creci = None
        
        try: #telefone primario do anunciante
            numero_anunciante_1 = json_object.get('account').get('phone').get('primary')
        except:
            numero_anunciante_1 = None
        
        try: #telefone secundario do anunciante
            numero_anunciante_2 = json_object.get('account').get('phone').get('mobile')
        except:
            numero_anunciante_2 = None
        
        #Url do anuncio do imovel
        url_anuncio = lista_url[pos]

        #Dicionario para guardar todas as variaveis
        data = {
            'id_ambiente':id_ambiente,                      #ID VivaReal
            'tipo_imovel':tipo_imovel,                      #Tipo de Imovel
            'novo_usado':novo_usado,                        #Condiçao do Imovel
            'titulo':titulo,                                #Titulo do anuncio
            'rua':rua,                                      #Numero na Rua
            'numero':numero,                                #numero da casa
            'bairro':bairro,                                #bairro
            'cidade':cidade,                                #cidade
            'estado':estado,                                #Estado
            'cep':int(cep),                                 #Cep
            'preco':float(preco),                           #Titulo do Anuncio
            'area_privativa':area_privativa,                #area construida
            'quartos':quartos,                              #Preço do Imovel
            'suites':suites,                                #  --   de Suites
            'garagens':garagens,                            #  --   de Vagas de Garagem
            'iptu':iptu,                                    #Iptu
            'taxa_condominio':taxa_condominio,              #Preço do Condominio
            'descricao':descricao,                          #Descriçao do Imovel
            'caracteristicas':caracteristicas,              #Caracteristicas do Imovel
            'data_anuncio':data_anuncio,                    #Data de Criaçao do Imovel
            'nome_anunciante':nome_anunciante,              #Nome do Anunciante
            'cod_anunciante':cod_anunciante,                #Id da Imobiliaria
            'numero_anunciante_1': numero_anunciante_1,     #Telefone Primario do Anunciante
            'numero_anunciante_2': numero_anunciante_2,     #Telefone Secundario do Anunciante
            'creci':creci,                                  #Numero de licença do Anunciante
            'status':status,                                #Status do Anuncio (Ativado/Desativado)
            'url_anuncio':url_anuncio                       #Url do Anuncio 
        }
        
        tempo = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        #Guarda as infos dos imoveis na tabela garimpo do banco de dados, e pega o id_garimpo gerado
        comando = f"""INSERT INTO garimpo (idambiente, ambiente, caminho , criadopor, criadoem, alteradopor, alteradoem) 
                        VALUES ("{id_ambiente}","VivaReal", "{url_anuncio}", "Gustavo", "{tempo}", "Gustavo", "{tempo}")"""
        cursor.execute(comando)
        conexao.commit()
        comando = """ SELECT LAST_INSERT_ID();"""
        cursor.execute(comando)
        id_garimpo = cursor.fetchall()
        id_garimpo = id_garimpo[0][0]
        

        tempo = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        #Guarda as infos na tabela garimpo dados
        for item in data.items():
            if item[1] is not None:    
                #Caso variavel do imovel seja tipo lista
                if isinstance(item[1],list):
                    for c in item[1]:
                        comando = f"""INSERT INTO garimpodados (idgarimpo , chave, valor , criadopor, criadoem, alteradopor, alteradoem) 
                                    VALUES ("{id_garimpo}","{traduz_palavra(c)}", "sim", "Gustavo", "{tempo}", "Gustavo", "{tempo}")"""
                        cursor.execute(comando)
                        conexao.commit()
                
                else:
                    comando = f"""INSERT INTO garimpodados (idgarimpo , chave, valor , criadopor, criadoem, alteradopor, alteradoem) 
                                    VALUES ("{id_garimpo}","{item[0]}", "{traduz_palavra(item[1])}", "Gustavo", "{tempo}", "Gustavo", "{tempo}")"""
                    cursor.execute(comando)
                    conexao.commit()
            else:
                pass


        #Salva as fotos e guarda os paths
        #Cria pasta para o imovel especifico
        directory = parent_dir / str(id_ambiente)
        directory.mkdir(exist_ok=True)

        contador = 1 #contador para ajudar no nomeamento das fotos

        for img in imagens: #Para cada tag/img na lista imagens
            url_img = img.find('img').get('src')                        #Acha a tag (img) e pega o conteudo de source
            url_img = url_img.replace("crop/142x80","fit-in/870x653")   #faz o tratamento necessario da string
                                                                        #faz um append na lista de urls
            #Download da Imagem
            #request da url da img
            r = requests.get(url_img,headers=headers)
            time.sleep(1)
            directory_imagem = directory / f'foto_{contador}.jpg'
            print(directory_imagem)
            #Cria arquivo jpg e escreve conteudo do request nele
            with open(directory_imagem,'wb') as f:
                f.write(r.content)
            contador +=1  #contador incrementa 1
            comando = f"""INSERT INTO garimpofotos (idambiente, ambiente, url , criadopor, criadoem, alteradopor, alteradoem) 
                            VALUES ("{id_ambiente}","VivaReal", "{directory_imagem}", "Gustavo", "{tempo}", "Gustavo", "{tempo}")"""
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

