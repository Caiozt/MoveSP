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

# Perguntar ao usuário quantos registros deseja ver (limite)
limite = input("Quantos registros deseja ver? (máximo 1000): ")

try:
    inicio = int(inicio)
    limite = int(limite)
    if inicio < 0 or limite <= 0:
        raise ValueError("Os valores devem ser positivos.")
    if limite > 1000:
        print("Limite máximo é 1000. Será usado 1000.")
        limite = 1000
except ValueError:
    print("Entrada inválida. Digite números inteiros válidos.")
    cursor.close()
    conn.close()
    exit()

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
    print(f"Mostrando {len(resultados)} registros a partir da linha {inicio}")

# Fechar a conexão
cursor.close()
conn.close()
