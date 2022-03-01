import requests

API_TOKEN='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NzM2ZDFmNmRlMGJiMmU5Njk3ZWY2OGZjMTE3MGJmMSIsInN1YiI6IjYyMGFhMjNlZWY4YjMyMDAxYjY5ZmRiZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bZFR-2sRj8ZrGxIQyZIqFTi8ESjxLQPYTvLb0CqfAUU'

def call_tmdb_api(endpoint):
    full_url=f'https://api.themoviedb.org/3/{endpoint}'
    headers={
        'Authorization':f'Bearer {API_TOKEN}'
    }
    response =requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f'movie/{list_type}')

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(f'movie/{movie_id}')

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f'movie/{movie_id}/credits')

def get_cast(movie_id,how_many):
    data=get_single_movie_cast(movie_id)
    return data['cast'][:how_many]




