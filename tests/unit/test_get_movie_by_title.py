
# TODO: Feature 3

from src.repositories.movie_repository import movie_repository_singleton

def test_movie_by_title():
    
    movie = movie_repository_singleton.create_movie('Star Wars', 'George Lucas', 5)
    #make sure movie tile is the same 
    assert movie.title == 'Star Wars'
    movie2 = movie_repository_singleton.create_movie('', 'George Lucas', 5)
    
    assert movie2.title == None
    movie_repository_singleton.get_all_movies().clear()

