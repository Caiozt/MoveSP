import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio",
    database="movesp"
)

cursor = conn.cursor()

# Consulta para contar compras ativas
query = """
SELECT COUNT(*)
FROM compras
WHERE status = 'ativo' AND Data_expiracao > NOW();
"""

cursor.execute(query)
resultado = cursor.fetchone()

print(f"Total de compras ativas: {resultado[0]}")

cursor.close()
conn.close()