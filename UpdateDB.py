
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(host="localhost", user="root", password="caio", database="movesp")
cursor = conn.cursor()

#atualiza os statu da compra'   \
update = """
    UPDATE compras
    SET status = 'expirado'
    WHERE status = 'ativo' AND data_expiracao <= NOW();"""

cursor.execute(update)
conn.commit()
cursor.close()
conn.close()