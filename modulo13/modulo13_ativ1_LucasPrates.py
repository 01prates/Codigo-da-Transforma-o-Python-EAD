from flask import Flask

app = Flask(__name__)

@app.route("/saudacao", methods=["GET"])
def saudacao():
    return "Olá, seja bem-vindo ao servidor Flask!"

if __name__ == "__main__":
    app.run(debug=True)