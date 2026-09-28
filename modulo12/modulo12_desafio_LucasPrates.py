from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola():
    return "Olá Mundo"

def test_ola():
    cliente = app.test_client()
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert resposta.data.decode("utf-8") == "Olá Mundo"