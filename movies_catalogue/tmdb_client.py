import requests

API_TOKEN='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NzM2ZDFmNmRlMGJiMmU5Njk3ZWY2OGZjMTE3MGJmMSIsInN1YiI6IjYyMGFhMjNlZWY4YjMyMDAxYjY5ZmRiZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.bZFR-2sRj8ZrGxIQyZIqFTi8ESjxLQPYTvLb0CqfAUU'

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_cast(movie_id,how_many):
    data=get_single_movie_cast(movie_id)
    return data['cast'][:how_many]




