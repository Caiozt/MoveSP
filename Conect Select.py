import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="caio", database="movesp")
cursor = conn.cursor()


cursor = conn.cursor()

# Consultar dados
cursor.execute("SELECT * FROM cliente")

# Obter todos os resultados
resultados = cursor.fetchall()

# Exibir os resultados
for linha in resultados:
    print(linha)

# Fechar a conexão
cursor.close()
conn.close()