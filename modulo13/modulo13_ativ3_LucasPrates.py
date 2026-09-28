from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def criar_banco():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)")
    conexao.commit()
    conexao.close()

criar_banco()

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    
    return jsonify({"mensagem": "Usuário salvo no banco de dados com sucesso!"}), 201

if __name__ == "__main__":
    app.run(debug=True)