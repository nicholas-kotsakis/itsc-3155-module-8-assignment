# TODO: Feature 2
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movies_page(test_app):
    # Assert webpage contents
    response = test_app.get('/movies/new')
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response.data
    
    data = {
        'title':'Not As Awesome Movie Title',
        'director':'Guy Person',
        'rating': 2
    }
    # Test POST response 
    # Get previous length to make sure the length only increased by 1
    prev_len = len(movie_repository_singleton.get_all_movies())
    response = test_app.post('/movies',data=data)
    saved_movies = movie_repository_singleton.get_all_movies()
    assert len(saved_movies) == prev_len + 1
    # Find index of new movie at end of array
    i = len(saved_movies) - 1
    assert saved_movies[i].title == data['title']
    assert saved_movies[i].director == data['director']
    assert saved_movies[i].rating == data['rating']
    movie_repository_singleton.get_all_movies().clear()