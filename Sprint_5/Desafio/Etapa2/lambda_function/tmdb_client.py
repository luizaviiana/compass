import requests
import time
import os

bearer_token = os.environ["TMDB_BEARER_TOKEN"]


headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json;charset=utf-8"
}

def buscar_ids_filmes_guerra():
    url_base = "https://api.themoviedb.org/3/discover/movie"
    pagina = 1
    filmes = []

    while True:
        params = {
            "language": "pt-BR",
            "with_genres": 10752,
            "sort_by": "popularity.desc",
            "vote_count.gte": 100,
            "vote_average.gte": 6.0,
            "page": pagina,
            "primary_release_date.gte": "1950-01-01"
        }

        response = requests.get(url_base, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Erro ao buscar página {pagina}: {response.status_code}")
            break

        dados = response.json()
        resultados = dados.get("results", [])
        if not resultados:
            break

        filmes.extend(resultados)
        print(f"Página {pagina} coletada com {len(resultados)} filmes.")
        pagina += 1

        if pagina > dados.get("total_pages", 1):
            break

        time.sleep(0.25)

    return [filme['id'] for filme in filmes]

def buscar_detalhes_filme(id_tmdb):
    url = f"https://api.themoviedb.org/3/movie/{id_tmdb}?language=pt-BR&append_to_response=credits,keywords,release_dates"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar detalhes do filme ID {id_tmdb}")
        return None
