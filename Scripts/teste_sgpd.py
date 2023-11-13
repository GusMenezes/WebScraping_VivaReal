import mysql.connector
import pandas as pd
import datetime

time = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
df = pd.read_csv("Exel_and_Csv_Files\Viva_Real_Scrap 26-10-2023.csv",sep=",")


conexao = mysql.connector.connect(
    host = '193.203.183.54',
    user = 'perdigueiro',
    password = 'V3nc3d0r3s@23',
    database = 'perdigueiro',
)

cursor = conexao.cursor()


for x in range(0,100):
    id_ambiente = df['ID_VivaReal'][x]/1000
    ambiente = 'VivaReal'
    caminho = df['Url_Place'][x]
    criadopor = 'Gustavo'
    criadoem = time
    alteradopor = 'Gustavo'
    alteradoem = time

    
    comando = f"""INSERT INTO garimpo (idambiente, ambiente, caminho , criadopor, criadoem, alteradopor, alteradoem) 
    VALUES ("{id_ambiente}","{ambiente}", "{caminho}", "{criadopor}", "{criadoem}", "{alteradopor}", "{alteradoem}")"""

    cursor.execute(comando)
    conexao.commit()



cursor.close()
conexao.close()