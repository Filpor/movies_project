import tmdb_client
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
    #Przygotowanie danych
    poster_api_path='some-poster-path'
    expected_default_size='w342'
    #Wywołanie kodu testowego
    poster_url=tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    #porównywanie wyników
    assert expected_default_size in poster_url

def test_get_movies_list(monkeypatch):
    mock_movies_list=['Movie 1','Movie 2']

    request_mock=Mock()
    response=request_mock.return_value
    response.json.return_value=mock_movies_list
    monkeypatch.setattr('tmdb_client.requests.get',request_mock)
    movies_list=tmdb_client.get_movies_list(list_type='popular')
    assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
    mock_single_movie=111111

    requests_mock=Mock()
    response=requests_mock.return_value
    response.json.return_value=mock_single_movie
    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)

    movie=tmdb_client.get_single_movie(movie_id=476669)
    assert movie==mock_single_movie

def test_get_single_movie_cast(monkeypatch):
    mock_cast={'adult': False, 'gender': 1, 'id': 9206, 
    'known_for_department': 'Acting', 'name': 'Neve Campbell', 
    'original_name': 'Neve Campbell', 'popularity': 25.569, 
    'profile_path': '/9fDbXBbrM6L10YrzDJUJowDt8U.jpg', 
    'cast_id': 17, 'character': 'Sidney Prescott', 
    'credit_id': '5f5a6b0cd8cc4a003ae4f3f1', 'order': 0}
    requests_mock=Mock()
    response=requests_mock.return_value
    response.json.return_value=mock_cast
    monkeypatch.setattr('tmdb_client.requests.get',requests_mock)

    cast=tmdb_client.get_single_movie_cast(movie_id=646385)
    assert cast == mock_cast




