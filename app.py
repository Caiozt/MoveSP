from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexão com o banco
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="caio",
        database="movesp"
    )

@app.route('/', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        data_nascimento = request.form['data']
        email = request.form['email']
        senha = request.form['senha']

        conn = conectar_banco()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO cliente (Nome, CPF, Data_nascimeto, Email, Senha)
                VALUES (%s, %s, %s, %s, %s)
            """, (nome, cpf, data_nascimento, email, senha))
            
            conn.commit()
        except mysql.connector.Error as err:
            print("Erro ao inserir:", err)
        finally:
            cursor.close()
            conn.close()

        return redirect('/')  # Redireciona para a mesma página após envio
    
    return render_template('Index.html')

if __name__ == '__main__':
    app.run(debug=True)
