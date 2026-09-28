from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def criar_banco():
    conexao = sqlite3.connect("blog.db")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Posts (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, conteudo TEXT)")
    conexao.commit()
    conexao.close()

criar_banco()

@app.route("/posts", methods=["POST"])
def criar_post():
    dados = request.get_json()
    titulo = dados.get("titulo")
    conteudo = dados.get("conteudo")
    
    conexao = sqlite3.connect("blog.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Posts (titulo, conteudo) VALUES (?, ?)", (titulo, conteudo))
    conexao.commit()
    conexao.close()
    
    return jsonify({"mensagem": "Post criado com sucesso!"}), 201

@app.route("/posts", methods=["GET"])
def listar_posts():
    conexao = sqlite3.connect("blog.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Posts")
    posts = [{"id": linha[0], "titulo": linha[1], "conteudo": linha[2]} for linha in cursor.fetchall()]
    conexao.close()
    
    return jsonify(posts), 200

if __name__ == "__main__":
    app.run(debug=True)