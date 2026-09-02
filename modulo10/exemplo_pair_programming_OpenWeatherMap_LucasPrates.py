import requests

def buscar_filme(nome_filme, api_key):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={nome_filme}&language=pt-BR"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        resultados = response.json().get("results", [])
        
        if not resultados:
            print("Nenhum filme encontrado com esse nome.")
            return

        # Pega o primeiro filme retornado na busca
        filme = resultados[0]
        titulo = filme.get("title")
        data_lancamento = filme.get("release_date", "N/A")
        sinopse = filme.get("overview", "Sinopse não disponível.")
        
        print(f"\n--- Título: {titulo} ---")
        print(f"Lançamento: {data_lancamento}")
        print(f"Sinopse: {sinopse}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API do TMDB: {e}")

# Substitua pela sua chave da API do TMDB
API_KEY_TMDB = "SUA_API_KEY_TMDB_AQUI"
filme_busca = input("Digite o nome de um filme: ")
buscar_filme(filme_busca, API_KEY_TMDB)