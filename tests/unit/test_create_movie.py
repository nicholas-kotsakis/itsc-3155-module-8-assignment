# TODO: Feature 2
from flask import request
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    title1 = "Awesome Movie Title"
    director1 = "Person Guy"
    rating1 = 3
    title2 = "Not As Awesome Movie Title"
    director2 = "Guy Person"
    rating2 = 1
    send_request = request.post("/movies",title=title1,director=director1,rating=rating1)
    saved_movies = movie_repository_singleton.get_all_movies()
    assert saved_movies[0].title == title1
    assert saved_movies[0].director == director1
    assert saved_movies[0].rating == rating1
    assert len(saved_movies) == 1
    send_request = request.post("/movies",title=title2,director=director2,rating=rating2)
    saved_movies = movie_repository_singleton.get_all_movies()
    assert saved_movies[1].title == title2
    assert saved_movies[1].director == director2
    assert saved_movies[1].rating == rating2
    assert len(saved_movies) == 2