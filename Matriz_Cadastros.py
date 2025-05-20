import mysql.connector
import random
import string
from faker import Faker
from datetime import datetime
from datetime import timedelta
import hashlib

conn = mysql.connector.connect(host="localhost", user="root", password="caio", database="movesp")
cursor = conn.cursor()

# Gerador de dados falsos
faker = Faker('pt_BR')
# Função para gerar CPF único formatado
def gerar_cpf():
    def dv(n):
        r = sum([(len(n)+1-i)*int(v) for i, v in enumerate(n)]) % 11
        return '0' if r < 2 else str(11 - r)
    n = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return '{}.{}.{}-{}'.format(n[:3], n[3:6], n[6:], dv(n + dv(n)))

# Função para gerar senha criptografada (simples hash)
def gerar_senha():
    senha = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return hashlib.sha256(senha.encode()).hexdigest()

def gerar_data_criacao():
    # Gera uma data entre 1º janeiro de 2022 e hoje
    inicio = datetime(2022, 1, 1)
    fim = datetime.now()
    delta = fim - inicio
    dias_aleatorios = random.randint(0, delta.days)
    data = inicio + timedelta(days=dias_aleatorios)
    return data.strftime('%Y-%m-%d %H:%M:%S')

# Inserindo os dados
for _ in range(10000):
    nome = faker.name()
    cpf = gerar_cpf()
    data_nascimento = faker.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
    email = faker.unique.email()
    senha = gerar_senha()
    data_criacao = gerar_data_criacao()

    try:
        cursor.execute("""
            INSERT INTO cliente (Nome, CPF, Data_nascimeto, Email, Senha, Data_criacao)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nome, cpf, data_nascimento, email, senha, data_criacao))
    except mysql.connector.IntegrityError as e:
        print("Erro ao inserir:", e)

# Confirmar e fechar
conn.commit()
cursor.close()
conn.close()
print("Inserção concluída.")