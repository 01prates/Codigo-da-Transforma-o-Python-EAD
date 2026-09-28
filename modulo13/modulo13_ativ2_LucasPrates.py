from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!", "dados": dados}), 201

if __name__ == "__main__":
    app.run(debug=True)