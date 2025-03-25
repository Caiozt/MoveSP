import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(host="localhost", user="root", password="caio1234", database="movesp")
cursor = conn.cursor()

query = """
    UPDATE compras
    SET status = 'expirado'
    WHERE status = 'ativo' AND data_expiracao <= NOW();
"""
cursor.execute(query)
conn.commit()
cursor.close()
conn.close()