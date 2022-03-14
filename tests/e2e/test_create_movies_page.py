# TODO: Feature 2
from flask import request
from app import app
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie(test_app):
    title1 = "Awesome Movie Title"
    director1 = "Person Guy"
    rating1 = 3
    title2 = "Not As Awesome Movie Title"
    director2 = "Guy Person"
    rating2 = 1
    # send_request = app.post('/movies',title=title1,director=director1,rating=rating1)
    # saved_movies = movie_repository_singleton.get_all_movies()
    # assert len(saved_movies) == 1
    # assert saved_movies[0].title == title1
    # assert saved_movies[0].director == director1
    # assert saved_movies[0].rating == rating1
    # send_request = request.post("/movies",title=title2,director=director2,rating=rating2)
    # saved_movies = movie_repository_singleton.get_all_movies()
    # assert len(saved_movies) == 2
    # assert saved_movies[1].title == title2
    # assert saved_movies[1].director == director2
    # assert saved_movies[1].rating == rating2