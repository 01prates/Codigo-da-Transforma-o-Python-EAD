import requests

cidade = "Sao Paulo"
chave_api = "SUA_CHAVE_API_AQUI"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

resposta = requests.get(url)
dados = resposta.json()

print("Temperatura:", dados["main"]["temp"])
print("Clima:", dados["weather"][0]["description"])