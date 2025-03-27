
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(host="localhost", user="root", password="caio", database="movesp")
cursor = conn.cursor()


update = """
    UPDATE cliente
    SET Email = 'caiosantos@gmail.com'
    WHERE ID = 1;
"""

#UPDATE compras
#    SET status = 'expirado'
#    WHERE status = 'ativo' AND data_expiracao <= NOW();

cursor.execute(update)
conn.commit()
cursor.close()
conn.close()