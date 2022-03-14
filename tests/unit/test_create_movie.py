# TODO: Feature 2
from flask import request
from app import app
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    title1, director1, rating1 = "Awesome Movie Title", "Person Guy", 3
    title2, director2, rating2 = "Not As Awesome Movie Title", "Guy Person", 1
    movie_repository_singleton.create_movie(title1,director1,rating1)
    saved_movies = movie_repository_singleton.get_all_movies()
    assert len(saved_movies) == 1
    assert saved_movies[0].title == title1
    assert saved_movies[0].director == director1
    assert saved_movies[0].rating == rating1
    movie_repository_singleton.create_movie(title2,director2,rating2)
    saved_movies = movie_repository_singleton.get_all_movies()
    assert len(saved_movies) == 2
    assert saved_movies[1].title == title2
    assert saved_movies[1].director == director2
    assert saved_movies[1].rating == rating2