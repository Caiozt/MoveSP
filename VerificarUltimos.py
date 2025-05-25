import mysql.connector

# Conectar ao banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio",
    database="movesp"
)
cursor = conn.cursor()

# Executar a consulta apenas com as colunas desejadas, ordenadas do mais recente para o mais antigo
cursor.execute("SELECT ID, Nome, CPF, Email FROM cliente ORDER BY ID DESC LIMIT 10")

# Obter nomes das colunas
colunas = [desc[0] for desc in cursor.description]

# Obter todos os resultados
resultados = cursor.fetchall()

# Exibir cabeçalhos
print("-" * 100)
print(" | ".join(f"{col:<20}" for col in colunas))
print("-" * 100)

# Exibir os dados formatados
for linha in resultados:
    print(" | ".join(f"{str(campo):<20}" for campo in linha))

print("-" * 100)

# Fechar a conexão
cursor.close()
conn.close()
