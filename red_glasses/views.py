from django.shortcuts import render
import requests

def index(request):
    popular_url = "https://api.themoviedb.org/3/movie/popular"

    params = {
        "api_key": "6cd101ecd178ac88ad307ea8fccdf574",
        "language": "ko",
        "page": "1",
        "region": "KR",
        }
    
    popular_response = requests.get(popular_url, params=params)
    popular_info = popular_response.json()
    popular_movies = sorted(popular_info['results'], key=lambda x: -x['vote_average'])
    for i, popular_movie in enumerate(popular_movies, start=1):
        popular_movie['rank'] = i


    now_playing_url = "https://api.themoviedb.org/3/movie/now_playing"

    now_playing_response = requests.get(now_playing_url, params=params)
    now_playing_info = now_playing_response.json()
    now_playing_movies = sorted(now_playing_info['results'], key=lambda x: -x['vote_average'])
    for i, now_playing_movie in enumerate(now_playing_movies, start=1):
        now_playing_movie['rank'] = i

    upcoming_url = "https://api.themoviedb.org/3/movie/upcoming"

    upcoming_response = requests.get(upcoming_url, params=params)
    upcoming_info = upcoming_response.json()
    upcoming_movies = sorted(upcoming_info['results'], key=lambda x: x['release_date'])

    context = {
        'popular_movies': popular_movies,
        'now_playing_movies': now_playing_movies,
        'upcoming_movies': upcoming_movies,
    }
    return render(request, 'index.html', context)