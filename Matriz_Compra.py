import mysql.connector
import random
from faker import Faker

faker = Faker('pt_BR')

conn = mysql.connector.connect(host="localhost", user="root", password="caio", database="movesp")
cursor = conn.cursor()

# Seleciona 30.000 clientes aleatórios de um total de 60.000
ids_clientes = random.sample(range(1, 40001), 30000)

# Mapas de duração por plano
duracoes = {1: 30, 2: 60, 3: 90}

for cliente_id in ids_clientes:
    plano_id = random.randint(1, 2)
    nome_cartao = faker.name()
    numero_cartao = random.randint(1000, 9999)
    expiracao_cartao = faker.date_between(start_date='+1y', end_date='+5y').strftime('%Y-%m-%d')
    cvc = random.randint(100, 999)
    data_compra = faker.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d %H:%M:%S')
    duracao = duracoes[plano_id]

    cursor.execute("""
        INSERT INTO Compras (cliente_id, Plano_id, Nome_cartao, Numero_cartao, Expiracao_cartao, CVC, Data_compra, Duracao_pl)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (cliente_id, plano_id, nome_cartao, numero_cartao, expiracao_cartao, cvc, data_compra, duracao))

conn.commit()
cursor.close()
conn.close()
print("Planos e compras inseridos com sucesso.")
