import mysql.connector

conexao = mysql.connector.connect(
    host = '193.203.183.54',
    user = 'perdigueiro',
    password = 'V3nc3d0r3s@23',
    database = 'perdigueiro',
)

cursor = conexao.cursor()

print(cursor)


cursor.close()
conexao.close()