import mysql.connector
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio1234",
    database="movesp"
)

cursor = conn.cursor()

query = """
SELECT DATE_FORMAT(data_compra, '%Y-%m') AS mes, SUM(preco) AS receita_total
FROM compras 
JOIN planos ON compras.plano_id = planos.id
WHERE status = 'ativo'
GROUP BY mes
ORDER BY mes;
"""

df = pd.read_sql(query, conn)
conn.close()


# Configurar estilo do gráfico
sns.set_theme(style="darkgrid")

# Criar gráfico de linha para receita mensal
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["mes"], y=df["receita_total"], marker="o", color="blue")

# Configurar rótulos
plt.xlabel("Mês")
plt.ylabel("Receita Total (R$)")
plt.title("Receita Mensal - Movesp")

plt.xticks(rotation=45)
plt.show()
