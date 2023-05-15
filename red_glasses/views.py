from django.shortcuts import render
from posts.models import Post, Comment
import requests

def index(request):
    popular_url = "https://api.themoviedb.org/3/movie/popular"

    params = {
        "api_key": "6cd101ecd178ac88ad307ea8fccdf574",
        "language": "ko",
        "page": "1",
        }
    
    popular_response = requests.get(popular_url, params=params)
    popular_info = popular_response.json()
    popular_movies = popular_info['results'][:5]
    for i, popular_movie in enumerate(popular_movies, start=1):
        popular_movie['rank'] = i

    context = {
        'popular_movies': popular_movies,
    }
    return render(request, 'index.html', context)