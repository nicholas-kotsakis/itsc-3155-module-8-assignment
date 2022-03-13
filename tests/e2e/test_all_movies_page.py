# TODO: Feature 1
from src.repositories.movie_repository import movie_repository_singleton

def test_list_all_movies(test_app):
    movie_repository_singleton.create_movie('Test Movie Title','Test Director',5)
    response = test_app.get('/movies')
    assert b"Test Movie Title" in response.data
    test_string = str(response.data)
    assert test_string.count('<i class=\"fas fa-star\" style=\"color: gold;\"></i>') == 5
    assert b"Test Director" in response.data
    movie_repository_singleton.get_all_movies().clear()



