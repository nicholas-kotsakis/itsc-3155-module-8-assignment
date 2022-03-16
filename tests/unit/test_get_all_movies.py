# TODO: Feature 1
from src.repositories.movie_repository import movie_repository_singleton

def f():
    movie_repository_singleton.create_movie('Test Movie Title','Test Director',5)
    return(movie_repository_singleton.get_all_movies())

def test_function():
    movies = f()
    assert len(movies) == 1
    assert movies[0].title == 'Test Movie Title'
    assert movies[0].rating == 5
    movies = f()
    assert len(movies) == 2
    movie_repository_singleton.get_all_movies().clear()
