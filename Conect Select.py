import mysql.connector

# Conectar ao banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio",
    database="movesp"
)
cursor = conn.cursor()

# Executar a consulta
cursor.execute("SELECT * FROM cliente")

# Obter nomes das colunas
colunas = [desc[0] for desc in cursor.description]

# Obter todos os resultados
resultados = cursor.fetchall()

# Exibir cabeçalhos
print("-" * 120)
print(" | ".join(f"{col:<20}" for col in colunas))
print("-" * 120)

# Exibir os dados formatados
for linha in resultados:
    print(" | ".join(f"{str(campo):<20}" for campo in linha))

print("-" * 120)

# Fechar a conexão
cursor.close()
conn.close()