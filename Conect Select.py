import mysql.connector

# Conectar ao banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio",
    database="movesp"
)
cursor = conn.cursor()

# Perguntar ao usuário de qual linha começar (offset)
inicio = input("A partir de qual linha deseja ver os dados? (ex: 0 para início): ")

try:
    inicio = int(inicio)
    if inicio < 0:
        raise ValueError("O valor deve ser 0 ou maior.")
except ValueError:
    print("Entrada inválida. Digite um número inteiro válido.")
    cursor.close()
    conn.close()
    exit()

# Definir limite fixo de 1000 registros
limite = 1000

# Executar a consulta com OFFSET e LIMIT
sql = "SELECT ID, Nome, CPF, Email FROM cliente LIMIT %s OFFSET %s"
cursor.execute(sql, (limite, inicio))

# Obter nomes das colunas
colunas = [desc[0] for desc in cursor.description]

# Obter todos os resultados
resultados = cursor.fetchall()

# Se não houver resultados
if not resultados:
    print("Nenhum dado encontrado para esse intervalo.")
else:
    # Exibir cabeçalhos
    print("-" * 100)
    print(" | ".join(f"{col:<20}" for col in colunas))
    print("-" * 100)

    # Exibir os dados formatados
    for linha in resultados:
        print(" | ".join(f"{str(campo):<20}" for campo in linha))

    print("-" * 100)
    print(f"Mostrando até 1000 registros a partir da linha {inicio}")

# Fechar a conexão
cursor.close()
conn.close()
