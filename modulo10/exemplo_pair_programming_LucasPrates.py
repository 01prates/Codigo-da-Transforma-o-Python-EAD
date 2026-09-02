import requests

def obter_previsao_tempo(cidade, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    
    try:
        # Atividade 1: Requisição HTTP com timeout
        response = requests.get(url, timeout=5)
        
        # Atividade 3: Dispara exceção para códigos de erro HTTP (4xx e 5xx)
        response.raise_for_status() 
        
        dados = response.json()
        
        # Atividade 2: Filtragem e exibição dos dados formatados
        temperatura = dados["main"]["temp"]
        sensacao = dados["main"]["feels_like"]
        humidade = dados["main"]["humidity"]
        descricao = dados["weather"][0]["description"]
        
        print(f"\n--- Clima em {cidade.title()} ---")
        print(f"Temperatura: {temperatura}°C")
        print(f"Sensação Térmica: {sensacao}°C")
        print(f"Umidade: {humidade}%")
        print(f"Condição: {descricao.capitalize()}")

    # Atividade 3: Tratamento de exceções de rede e status HTTP
    except requests.exceptions.Timeout:
        print("Erro: A conexão demorou muito para responder (Timeout).")
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print("Erro: Cidade não encontrada. Verifique o nome digitado.")
        elif response.status_code == 401:
            print("Erro: Chave de API ainda não foi ativada ou é inválida. Aguarde alguns minutos e tente novamente.")
        else:
            print(f"Erro HTTP: {err}")
    except requests.exceptions.RequestException:
        print("Erro: Falha na conexão de rede.")

# Sua chave de API configurada
API_KEY = "5a1c9b35c163ad66996470ec8a33a6f1"

cidade = input("Digite o nome da cidade: ")
obter_previsao_tempo(cidade, API_KEY)