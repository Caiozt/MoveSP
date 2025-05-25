import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="caio",
    database="movesp"
)

cursor = conn.cursor()

print("Escolha a opção:")
print("1 - Ver resumo de todas as compras")
print("2 - Ver somente compras ativas")

opcao = input("Digite 1 ou 2: ")

if opcao == '1':
    query = "SELECT ID, Nome_cliente, Nome_plano, status_atual FROM compras_resumida;"
elif opcao == '2':
    query = "SELECT ID, Nome_cliente, Nome_plano, status_atual FROM compras_ativas;"
else:
    print("Opção inválida.")
    cursor.close()
    conn.close()
    exit()

cursor.execute(query)
colunas = [desc[0] for desc in cursor.description]
resultados = cursor.fetchall()

print("-" * 90)
print(f"{colunas[0]:<8} | {colunas[1]:<25} | {colunas[2]:<30} | {colunas[3]:<20}")
print("-" * 90)

for linha in resultados:
    print(f"{str(linha[0]):<8} | {str(linha[1]):<30} | {str(linha[2]):<25} | {str(linha[3]):<20}")

print("-" * 90)

cursor.close()
conn.close()
