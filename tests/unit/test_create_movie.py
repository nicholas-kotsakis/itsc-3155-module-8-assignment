# TODO: Feature 2
from turtle import title
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    data = {
        'title':'Awesome Movie Title',
        'director':'Person Guy',
        'rating': 5
    }
    # Get previous length to make sure the length only increased by 1
    prev_len = len(movie_repository_singleton.get_all_movies())
    # Test create_movie function
    movie_repository_singleton.create_movie(data['title'],data['director'],data['rating'])
    saved_movies = movie_repository_singleton.get_all_movies()
    assert len(saved_movies) == prev_len + 1
    # Find index of new movie at end of array
    i = len(saved_movies) - 1
    assert saved_movies[i].title == data['title']
    assert saved_movies[i].director == data['director']
    assert saved_movies[i].rating == data['rating']